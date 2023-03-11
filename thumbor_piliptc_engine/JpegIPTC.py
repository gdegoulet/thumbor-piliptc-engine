from io import BytesIO
import contextlib
import os
import shutil
import sys
import tempfile
from struct import pack, unpack
import json

class EOFException(Exception):
    def __init__(self, *args):
        super().__init__(self)
        self._str = '\n'.join(args)

    def __str__(self):
        return self._str


class JpegIPTC:
    c_marker_err = {0: "Marker scan failed",
                    0xd9: "Marker scan hit EOI (end of image) marker",
                    0xda: "Marker scan hit start of image data"}

    c_charset = {100: 'iso8859_1', 101: 'iso8859_2', 109: 'iso8859_3',
                 110: 'iso8859_4', 111: 'iso8859_5', 125: 'iso8859_7',
                 127: 'iso8859_6', 138: 'iso8859_8',
                 196: 'utf_8'}
    c_charset_r = {v: k for k, v in c_charset.items()}
    
    
    def _ord3(self,x):
        return x if isinstance(x, int) else ord(x)

    def _read_exactly(self,bytesio_obj,length):
        buf = bytesio_obj.read(length)
        if buf is None or len(buf) < length:
            raise EOFException('read_exactly: %s' % str(bytesio_obj))
        return buf

    def _seek_exactly(self,bytesio_obj, length):
        pos = bytesio_obj.tell()
        bytesio_obj.seek(length, 1)
        if bytesio_obj.tell() - pos != length:
            raise EOFException('seek_exactly')

    def _jpeg_get_variable_length(self,bytesio_obj):
        try:
            length = unpack('!H', self._read_exactly(bytesio_obj, 2))[0]
        except EOFException:
            return 0
        # Length includes itself, so must be at least 2
        if length < 2:
            return 0
        return length - 2

    def _jpeg_next_marker(self,bytesio_obj):
        # Find 0xff byte. We should already be on it.
        try:
            byte = self._read_exactly(bytesio_obj, 1)
            while self._ord3(byte) != 0xff:
                byte = self._read_exactly(bytesio_obj, 1)
            # Now skip any extra 0xffs, which are valid padding.
            while True:
                byte = self._read_exactly(bytesio_obj, 1)
                if self._ord3(byte) != 0xff:
                    break
        except EOFException:
            return None
        # byte should now contain the marker id.
        return byte

    def _jpeg_skip_variable(self,bytesio_obj,rSave=None):
        # Get the marker parameter length count
        length = self._jpeg_get_variable_length(bytesio_obj)
        if length == 0:
            return None

        # Skip remaining bytes
        if rSave is not None:
            try:
                temp = self._read_exactly(bytesio_obj, length)
            except EOFException:
                return None
        else:
            # Just seek
            try:
                self._seek_exactly(bytesio_obj, length)
            except EOFException:
                return None
        return (rSave is not None and [temp] or [True])[0]        

    def _jpegScan(self,bytesio_obj):
        SOI = 0xd8  # Start of image
        # Skip past start of file marker
        try:
            (ff, soi) = self._read_exactly(bytesio_obj, 2)
        except EOFException:
            return None
        if not (self._ord3(ff) == 0xff and self._ord3(soi) == SOI):
            self.error = "JpegScan: invalid start of file"
            return None     
        # Scan for the APP13 marker which will contain our IPTC info (I hope).
        while True:
            err = None
            marker = self._jpeg_next_marker(bytesio_obj)
            if self._ord3(marker) == 0xed: # 0xed # Photoshop3 IPTC (APP13)
                break  # 237

            err = self.c_marker_err.get(self._ord3(marker), None)
            if err is None and self._jpeg_skip_variable(bytesio_obj) == 0:
                err = "jpeg_skip_variable failed"
            if err is not None:
                self.error = err
                return None
        return self._blindScan(bytesio_obj, MAX=self._jpeg_get_variable_length(bytesio_obj))

    def _blindScan(self,bytesio_obj,MAX=819200):
        offset = 0
        while offset <= MAX:
            try:
                temp = self._read_exactly(bytesio_obj, 1)
            except EOFException:
                return None
            # look for tag identifier 0x1c
            if self._ord3(temp) == 0x1c:
                # if we found that, look for record 2, dataset 0
                # (record version number)
                (record, dataset) = bytesio_obj.read(2)
                if record == 1 and dataset == 90:
                    # found character set's record!
                    try:
                        temp = self._read_exactly(bytesio_obj, self._jpeg_get_variable_length(bytesio_obj))
                        try:
                            cs = unpack('!H', temp)[0]
                        except Exception:  # TODO better exception
                            cs = None
                        if cs in self.c_charset:
                            self.inp_charset = self.c_charset[cs]
                    except EOFException:
                        pass

                elif record == 2:
                    # found it. seek to start of this tag and return.
                    try:  # seek rel to current position
                        self._seek_exactly(bytesio_obj, -3)
                    except EOFException:
                        return None
                    return offset

                else:
                    # didn't find it. back up 2 to make up for
                    # those reads above.
                    try:  # seek rel to current position
                        self._seek_exactly(bytesio_obj, -2)
                    except EOFException:
                        return None

            # no tag, keep scanning
            offset += 1
        return False
            

    def _scanToFirstIMMTag(self,bytesio_obj):
        if self.is_jpeg:
            return self._jpegScan(bytesio_obj)
        else:
            return self._blindScan(bytesio_obj)

    def _file_is_jpeg(self,bytesio_obj):
        SOI = 0xd8  # Start of image
        bytesio_obj.seek(0)
        ered = False
        try:
            (ff, soi) = bytesio_obj.read(2)
            if not (ff == 0xff and soi == SOI):
                ered = False
            else:
                # now check for APP0 marker. I'll assume that anything with a
                # SOI followed by APP0 is "close enough" for our purposes.
                # (We're not dinking with image data, so anything following
                # the Jpeg tagging system should work.)
                (ff, app0) = bytesio_obj.read(2)
                ered = ff == 0xff
        finally:
            bytesio_obj.seek(0)
            return ered
        return ered

    def _RawcollectIIMInfo(self, bytesio_obj):
        # NOTE: file should already be at the start of the first
        # IPTC code: record 2, dataset 0.
        bio = BytesIO()
        while True:
            try:
                header = self._read_exactly(bytesio_obj, 5)
            except EOFException:
                return bio
            bio.write(header)

            (tag, record, dataset, length) = unpack("!BBBH", header)
            # bail if we're past end of IIM record 2 data
            if not (tag == 0x1c and record == 2):
                return bio
            value = bytesio_obj.read(length)
            bio.write(value)

        return bio

    def _collect_adobe_parts(self,data):
        """Part APP13 contains yet another markup format, one defined by
        Adobe.  See"File Formats Specification" in the Photoshop SDK
        (avail from www.adobe.com). We must take
        everything but the IPTC data so that way we can write the file back
        without losing everything else Photoshop stuffed into the APP13
        block."""
        assert isinstance(data, bytes)
        length = len(data)
        offset = 0
        out = []
        # Skip preamble
        offset = len('Photoshop 3.0 ')
        # Process everything
        while offset < length:
            # Get OSType and ID
            (ostype, id1, id2) = unpack("!LBB", data[offset:offset + 6])
            offset += 6
            if offset >= length:
                break

            # Get pascal string
            stringlen = unpack("B", data[offset:offset + 1])[0]
            offset += 1
            if offset >= length:
                break

            string = data[offset:offset + stringlen]
            offset += stringlen

            # round up if odd
            if (stringlen % 2 != 0):
                offset += 1
            # there should be a null if string len is 0
            if stringlen == 0:
                offset += 1
            if offset >= length:
                break

            # Get variable-size data
            size = unpack("!L", data[offset:offset + 4])[0]
            offset += 4
            if offset >= length:
                break

            var = data[offset:offset + size]
            offset += size
            if size % 2 != 0:
                offset += 1  # round up if odd

            # skip IIM data (0x0404), but write everything else out
            if not (id1 == 4 and id2 == 4):
                out.append(pack("!LBB", ostype, id1, id2))
                out.append(pack("B", stringlen))
                out.append(string)
                if stringlen == 0 or stringlen % 2 != 0:
                    out.append(pack("B", 0))
                out.append(pack("!L", size))
                out.append(var)
                out = [b''.join(out)]
                if size % 2 != 0 and len(out[0]) % 2 != 0:
                    out.append(pack("B", 0))
        return b''.join(out)        

    def _jpeg_collect_file_parts(self,discard_app_parts=False):
        SOI = 0xd8  # Start of image
        APP0 = 0xe0  # Exif
        APP1 = 0xe1  # Exif
        APP13 = 0xed  # Photoshop3 IPTC
        COM = 0xfe  # Comment
        SOS = 0xda  # Start of scan
        EOI = 0xd9  # End of image

        adobeParts = b''
        start = []
        self.bytesio_obj.seek(0)
        (ff, soi) = self.bytesio_obj.read(2)
        if not (self._ord3(ff) == 0xff and self._ord3(soi) == SOI):
            raise Exception('invalid start of file, is it a Jpeg?')
        # Begin building start of file
        start.append(pack('BB', 0xff, SOI))  # pack('BB', ff, soi)
        # Get first marker. This *should* be APP0 for JFIF or APP1 for EXIF
        marker = ord(self._jpeg_next_marker(self.bytesio_obj))
        while marker != APP0 and marker != APP1:
            # print('bad first marker: %02X, skipping it' % marker)
            marker = ord(self._jpeg_next_marker(self.bytesio_obj))
            if marker is None:
                break
        # print('first marker: %02X %02X' % (marker, APP0))
        app0data = b''
        app0data = self._jpeg_skip_variable(self.bytesio_obj, app0data)
        if app0data is None:
            raise Exception('jpeg_skip_variable failed')
        
        if marker == APP0 or not discard_app_parts:
            # Always include APP0 marker at start if it's present.
            start.append(pack('BB', 0xff, marker))
            # Remember that the length must include itself (2 bytes)
            start.append(pack('!H', len(app0data) + 2))
            start.append(app0data)
        else:
            # Manually insert APP0 if we're trashing application parts, since
            # all JFIF format images should start with the version block.
            start.append(pack("BB", 0xff, APP0))
            start.append(pack("!H", 16))    # length (including these 2 bytes)
            start.append(b'JFIF')  # format
            start.append(pack("BB", 1, 2))  # call it version 1.2 (current JFIF)
            start.append(pack('8B', 0, 0, 0, 0, 0, 0, 0, 0))  # zero everything else
        
        # Now scan through all markers in file until we hit image data or
        # IPTC stuff.
        end = []
        while True:
            marker = self._jpeg_next_marker(self.bytesio_obj)
            if marker is None or self._ord3(marker) == 0:
                raise Exception('Marker scan failed')
            # Check for end of image
            elif self._ord3(marker) == EOI:
                end.append(pack("BB", 0xff, EOI))
                break
            # Check for start of compressed data
            elif self._ord3(marker) == SOS:
                end.append(pack("BB", 0xff, SOS))
                break
            partdata = b''
            partdata = self._jpeg_skip_variable(self.bytesio_obj, partdata)
            if not partdata:
                raise Exception('jpeg_skip_variable failed')
            partdata = bytes(partdata)
            # Take all parts aside from APP13, which we'll replace ourselves.
            if discard_app_parts and self._ord3(marker) >= APP0 and self._ord3(marker) <= 0xef:
                # Skip all application markers, including Adobe parts
                adobeParts = b''
            elif self._ord3(marker) == APP13:
                # Collect the adobe stuff from part 13
                adobeParts = self._collect_adobe_parts(partdata)
                break
            else:
                # Append all other parts to start section
                start.append(pack("BB", 0xff, self._ord3(marker)))
                start.append(pack("!H", len(partdata) + 2))
                start.append(partdata)

        # Append rest of file to end
        while True:
            buff = self.bytesio_obj.read(8192)
            if buff is None or len(buff) == 0:
                break
            end.append(buff)
        return (b''.join(start), b''.join(end), adobeParts)

    def _photoshopIIMBlock(self, otherparts, data):
        """Assembles the blob of Photoshop "resource data" that includes our
        fresh IIM data (from PackedIIMData) and the other Adobe parts we
        found in the file, if there were any."""
        APP13 = 0xed  # Photoshop3 IPTC
        out = []
        assert isinstance(data, bytes)
        resourceBlock = [b"Photoshop 3.0"]
        resourceBlock.append(pack("B", 0))
        # Photoshop identifier
        resourceBlock.append(b"8BIM")
        # 0x0404 is IIM data, 00 is required empty string
        resourceBlock.append(pack("BBBB", 0x04, 0x04, 0, 0))
        # length of data as 32-bit, network-byte order
        resourceBlock.append(pack("!L", len(data)))
        # Now tack data on there
        resourceBlock.append(data)
        # Pad with a blank if not even size
        if len(data) % 2 != 0:
            resourceBlock.append(pack("B", 0))
        # Finally tack on other data
        if otherparts is not None:
            resourceBlock.append(otherparts)
        resourceBlock = b''.join(resourceBlock)
        out.append(pack("BB", 0xff, APP13))  # Jpeg start of block, APP13
        out.append(pack("!H", len(resourceBlock) + 2))  # length
        out.append(resourceBlock)
        return b''.join(out)

    def __init__(self, data):
        self.error = None
        self.raw_iptc = None
        bytesio_obj = BytesIO()
        bytesio_obj.write(data)
        self.bytesio_obj = bytesio_obj
        self.is_jpeg = self._file_is_jpeg(bytesio_obj)
        datafound = self._scanToFirstIMMTag(bytesio_obj)
        if datafound:
            self.raw_iptc = self._RawcollectIIMInfo(bytesio_obj).getvalue()

    def set_raw_iptc(self,rawdata):
        self.raw_iptc = rawdata

    def dump(self):
        if not self.is_jpeg:
            return None
        jpeg_parts = self._jpeg_collect_file_parts()
        if jpeg_parts is None:
            raise Exception('jpeg_collect_file_parts failed: %s' % self.error)
        (start, end, adobe) = jpeg_parts
        tmpfh = BytesIO()
        tmpfh.write(start)
        data = self._photoshopIIMBlock(adobe, self.raw_iptc)
        tmpfh.write(data)
        tmpfh.write(end)
        tmpfh.flush()
        tmpfh.seek(0)
        return tmpfh.read()
