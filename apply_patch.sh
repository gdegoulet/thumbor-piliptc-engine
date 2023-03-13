#!/bin/bash
dir=$(dirname $(readlink -f $0))
release=$1
if test "$release" = ""
then
  release=$(curl --silent "https://api.github.com/repos/thumbor/thumbor/releases" | grep '"tag_name":' | sed -E 's/.*"([^"]+)".*/\1/' | head -n1)
fi
echo "release=$release dir=$dir"
cd "$dir"
test ! -f patch.txt && exit 1 

if test ! -f "thumbor/$release/pil.py"
then
  ./fetch_last_pil.sh $release
fi

test ! -f "thumbor/$release/pil.py" && exit 1

cp "thumbor/$release/pil.py" "/tmp/pil.py.$$"
patch -p1 "/tmp/pil.py.$$" "$dir/patch.txt"
test $? -ne 0 && exit 1

sed -ri "s/^__version__.*$/__version__ = '$release.1'/" "/tmp/pil.py.$$"
cat "/tmp/pil.py.$$" > "$dir/thumbor_piliptc_engine/engine.py"
rm -f "/tmp/pil.py.$$"
echo OK

