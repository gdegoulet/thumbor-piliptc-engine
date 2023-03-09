# thumbor-piliptc-engine

thumbor-piliptc-engine is a patched version from the legacy Pil imaging engine for [thumbor][].


## Installation

You can install the package from [PyPI][] with `pip`:

    $ pip install git+https://github.com/gdegoulet/thumbor-piliptc-engine 

### Requirements
-   Python 3.7 or higher
-   git (for now, you can only install from github repository )
-   iptcinfo3 (configured as dependance)

```
root@44171bd2df65:/src# pip install     --no-cache-dir     --prefix="${PYTHONUSERBASE}" git+https://github.com/gdegoulet/thumbor-piliptc-engine

Collecting git+https://github.com/gdegoulet/thumbor-piliptc-engine
  Cloning https://github.com/gdegoulet/thumbor-piliptc-engine to /tmp/pip-req-build-wjke7sx1
  Running command git clone --filter=blob:none --quiet https://github.com/gdegoulet/thumbor-piliptc-engine /tmp/pip-req-build-wjke7sx1
  Resolved https://github.com/gdegoulet/thumbor-piliptc-engine to commit 1d177cb44867a1b6dd3bd4e79551106c61b49750
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Requirement already satisfied: thumbor in /app/lib/python3.11/site-packages (from thumbor-piliptc-engine==0.0.1) (7.4.7)
Requirement already satisfied: pillow in /app/lib/python3.11/site-packages (from thumbor-piliptc-engine==0.0.1) (9.4.0)
Collecting iptcinfo3
  Downloading IPTCInfo3-2.1.4-py3-none-any.whl (12 kB)
Requirement already satisfied: colorama==0.*,>=0.4.3 in /app/lib/python3.11/site-packages (from thumbor->thumbor-piliptc-engine==0.0.1) (0.4.6)
Requirement already satisfied: derpconf==0.*,>=0.8.3 in /app/lib/python3.11/site-packages (from thumbor->thumbor-piliptc-engine==0.0.1) (0.8.3)
Requirement already satisfied: libthumbor==2.*,>=2.0.2 in /app/lib/python3.11/site-packages (from thumbor->thumbor-piliptc-engine==0.0.1) (2.0.2)
Requirement already satisfied: piexif==1.*,>=1.1.3 in /app/lib/python3.11/site-packages (from thumbor->thumbor-piliptc-engine==0.0.1) (1.1.3)
Requirement already satisfied: pytz>=2019.3.0 in /app/lib/python3.11/site-packages (from thumbor->thumbor-piliptc-engine==0.0.1) (2022.7.1)
Requirement already satisfied: statsd==3.*,>=3.3.0 in /app/lib/python3.11/site-packages (from thumbor->thumbor-piliptc-engine==0.0.1) (3.3.0)
Requirement already satisfied: tornado==6.*,>=6.0.3 in /app/lib/python3.11/site-packages (from thumbor->thumbor-piliptc-engine==0.0.1) (6.2)
Requirement already satisfied: thumbor-plugins-gifv==0.*,>=0.1.2 in /app/lib/python3.11/site-packages (from thumbor->thumbor-piliptc-engine==0.0.1) (0.1.2)
Requirement already satisfied: webcolors==1.*,>=1.10.0 in /app/lib/python3.11/site-packages (from thumbor->thumbor-piliptc-engine==0.0.1) (1.11.1)
Requirement already satisfied: six in /app/lib/python3.11/site-packages (from derpconf==0.*,>=0.8.3->thumbor->thumbor-piliptc-engine==0.0.1) (1.16.0)
Building wheels for collected packages: thumbor-piliptc-engine
  Building wheel for thumbor-piliptc-engine (pyproject.toml) ... done
  Created wheel for thumbor-piliptc-engine: filename=thumbor_piliptc_engine-0.0.1-py3-none-any.whl size=8416 sha256=368c59be3be675c00ea6d5f6aa33bb095bcf671a0303f9493cd9e950f7c7abad
  Stored in directory: /tmp/pip-ephem-wheel-cache-5fa3dug5/wheels/21/64/25/c294a71c2e9a294e2398ae7f49eb07e222d609cbc89c446f74
Successfully built thumbor-piliptc-engine
Installing collected packages: iptcinfo3, thumbor-piliptc-engine
Successfully installed iptcinfo3-2.1.4 thumbor-piliptc-engine-0.0.1
```


## Usage

To use this engine with thumbor, define `thumbor_piliptc_engine` as the imaging
engine in `thumbor.conf`:

```python
ENGINE = "thumbor_piliptc_engine"
```


## Example


```
wget https://i.f1g.fr/media/cms/509x286_crop/2022/11/21/76bde3fc961f0fa8733756922d1e2ed06311d804ec38b89dc60d6ba36d30e046.jpg


iptc 76bde3fc961f0fa8733756922d1e2ed06311d804ec38b89dc60d6ba36d30e046.jpg
76bde3fc961f0fa8733756922d1e2ed06311d804ec38b89dc60d6ba36d30e046.jpg:
 Tag      Name                 Type      Size  Value
 -------- -------------------- --------- ----  -----
 1:000    Model Version        Short        2  2
 1:020    File Format          Short        2  1
 1:022    File Version         Short        2  2
 1:030    Service Identifier   String       9  AFP-PHOTO
 1:040    Envelope Number      NumString    8  12345678
 1:060    Envelope Priority    NumString    1  5
 1:070    Date Sent            Date         8  20221120
 1:080    Time Sent            Time        11  210118+0000
 1:090    Coded Character Set  Binary       3  1b 2d 41
 1:100    Unique Name of Objec String      11  AFP_32PC4R2
 2:000    Record Version       Short        2  2
 2:005    Object Name          String      27  UKRAINE-RUSSIA-WAR-CONFLICT
 2:010    Urgency              NumString    1  5
 2:012:00 Subject Reference    String      45  IPTC:16009000:unrest, conflicts and  war:war:
 2:012:01 Subject Reference    String      41  IPTC:16000000:unrest, conflicts and  war:
 2:015    Category             String       3  WAR
 2:020    Supplemental Categor String       3  war
 2:025:00 Keywords             String       3  war
 2:025:01 Keywords             String      10  Horizontal
 2:055    Date Created         Date         8  20221120
 2:060    Time Created         Time        11  152935+0300
 2:062    Digital Creation Dat Date         8  20221120
 2:063    Digital Creation Tim Time        11  152935+0300
 2:065    Originating Program  String      22  g2mapping/libg2 3.9.39
 2:070    Program Version      String       6  3.9.15
 2:080    By-line              String      12  BULENT KILIC
 2:085    By-line Title        String       3  STF
 2:090    City                 String      12  Chornobaivka
 2:100    Country Code         String       3  UKR
 2:101    Country Name         String       7  Ukraine
 2:110    Credit               String       3  AFP
 2:115    Source               String       3  AFP
 2:116    Copyright Notice     String      16  AFP or licensors
 2:120    Caption/Abstract     String     242  A Ukrainian soldier walks in front of a destroyed building of the International Airport of Kherson in the village of Chornobaivka, outskirts of Kherson, on November 20, 2022, amid the Russian invasion of Ukraine. (Photo by BULENT KILIC / AFP)
 2:135    Language Identifier  String       2  EN



wget -O test.jpg "http://localhost:8901/unsafe/filters:quality(60)/i.f1g.fr/media/cms/509x286_crop/2022/11/21/76bde3fc961f0fa8733756922d1e2ed06311d804ec38b89dc60d6ba36d30e046.jpg"
--2023-03-09 19:05:53--  http://localhost:8901/unsafe/filters:quality(60)/i.f1g.fr/media/cms/509x286_crop/2022/11/21/76bde3fc961f0fa8733756922d1e2ed06311d804ec38b89dc60d6ba36d30e046.jpg
Resolving localhost (localhost)... 127.0.0.1
Connecting to localhost (localhost)|127.0.0.1|:8901... connected.
HTTP request sent, awaiting response... 200 OK
Length: 31970 (31K) [image/jpeg]
Saving to: 'test.jpg'

test.jpg                                                  100%[===================================================================================================================================>]  31,22K  --.-KB/s    in 0s

2023-03-09 19:05:53 (348 MB/s) - 'test.jpg' saved [31970/31970]

iptc test.jpg
test.jpg:
 Tag      Name                 Type      Size  Value
 -------- -------------------- --------- ----  -----
 2:000    Record Version       Short        2  4
 2:020    Supplemental Categor String       3  war
 2:025:00 Keywords             String       3  war
 2:025:01 Keywords             String      10  Horizontal
 2:005    Object Name          String      27  UKRAINE-RUSSIA-WAR-CONFLICT
 2:010    Urgency              NumString    1  5
 2:012    Subject Reference    String      41  IPTC:16000000:unrest, conflicts and  war:
 2:015    Category             String       3  WAR
 2:055    Date Created         Date         8  20221120
 2:060    Time Created         Time        11  152935+0300
 2:062    Digital Creation Dat Date         8  20221120
 2:063    Digital Creation Tim Time        11  152935+0300
 2:065    Originating Program  String      22  g2mapping/libg2 3.9.39
 2:070    Program Version      String       6  3.9.15
 2:080    By-line              String      12  BULENT KILIC
 2:085    By-line Title        String       3  STF
 2:090    City                 String      12  Chornobaivka
 2:100    Country Code         String       3  UKR
 2:101    Country Name         String       7  Ukraine
 2:110    Credit               String       3  AFP
 2:115    Source               String       3  AFP
 2:116    Copyright Notice     String      16  AFP or licensors
 2:120    Caption/Abstract     String     242  A Ukrainian soldier walks in front of a destroyed building of the International Airport of Kherson in the village of Chornobaivka, outskirts of Kherson, on November 20, 2022, amid the Russian invasion of Ukraine. (Photo by BULENT KILIC / AFP)
 2:135    Language Identifier  String       2  EN
```

## Logs


```
root@44171bd2df65:/src# thumbor --port=8000 --conf=/usr/src/app/thumbor.conf -l DEBUG
2023-03-09 18:05:48 root:DEBUG thumbor starting at 0.0.0.0:8000
2023-03-09 18:05:48 asyncio:DEBUG Using selector: EpollSelector
2023-03-09 18:05:53 thumbor:DEBUG METRICS: inc: response.count:1
2023-03-09 18:05:53 thumbor:DEBUG METRICS: inc: response.none_smart:1
2023-03-09 18:05:53 thumbor:DEBUG METRICS: timing: response.none_smart:0
2023-03-09 18:05:53 thumbor:DEBUG [RESULT_STORAGE] getting from /data/thumbor/result_storage/default/16/10/fc6d87db0af8192db5a48d82b016d4c28918
2023-03-09 18:05:53 thumbor:DEBUG [RESULT_STORAGE] image not found at /data/thumbor/result_storage/default/16/10/fc6d87db0af8192db5a48d82b016d4c28918
2023-03-09 18:05:53 thumbor:DEBUG METRICS: timing: result_storage.incoming_time:0
2023-03-09 18:05:53 thumbor:DEBUG METRICS: inc: result_storage.miss:1
2023-03-09 18:05:53 thumbor:DEBUG METRICS: inc: storage.miss:1
2023-03-09 18:05:53 thumbor:DEBUG METRICS: timing: original_image.fetch.200.i_f1g_fr:47
2023-03-09 18:05:53 thumbor:DEBUG METRICS: inc: original_image.fetch.200.i_f1g_fr:1
2023-03-09 18:05:53 thumbor:DEBUG METRICS: inc: original_image.status.200:1
2023-03-09 18:05:53 thumbor:DEBUG METRICS: inc: original_image.status.200.i_f1g_fr:1
2023-03-09 18:05:53 thumbor:DEBUG METRICS: inc: original_image.response_bytes:38698
2023-03-09 18:05:53 thumbor:DEBUG IPTC_PASSTHROUGH original image saved as /tmp/tmp3shuu1c0.original
2023-03-09 18:05:53 thumbor:DEBUG IPTC_PASSTHROUGH removing /tmp/tmp3shuu1c0.original
2023-03-09 18:05:53 thumbor:DEBUG METRICS: timing: iptc_passthrough_create_image.time:4
2023-03-09 18:05:53 thumbor:DEBUG creating tempfile for i.f1g.fr/media/cms/509x286_crop/2022/11/21/76bde3fc961f0fa8733756922d1e2ed06311d804ec38b89dc60d6ba36d30e046.jpg in /data/thumbor/storage/c8/a265b39d5bec5b40ca5a3714d34fbc04be5aae.7284027584e04272bc29e4711fb437ef...
2023-03-09 18:05:53 thumbor:DEBUG moving tempfile /data/thumbor/storage/c8/a265b39d5bec5b40ca5a3714d34fbc04be5aae.7284027584e04272bc29e4711fb437ef to /data/thumbor/storage/c8/a265b39d5bec5b40ca5a3714d34fbc04be5aae...
2023-03-09 18:05:53 thumbor:DEBUG No image format specified. Retrieving from the image extension: .jpg.
2023-03-09 18:05:53 thumbor:DEBUG Content Type of image/jpeg detected.
2023-03-09 18:05:53 thumbor:DEBUG IPTC_PASSTHROUGH saving result image to /tmp/tmpcn25mo6d.result
2023-03-09 18:05:53 thumbor:DEBUG IPTC_PASSTHROUGH reading new results from temporary file /tmp/tmpcn25mo6d.result
2023-03-09 18:05:53 thumbor:DEBUG IPTC_PASSTHROUGH removing /tmp/tmpcn25mo6d.result
2023-03-09 18:05:53 thumbor:DEBUG IPTC_PASSTHROUGH done
2023-03-09 18:05:53 thumbor:DEBUG METRICS: timing: iptc_passthrough_read.time:6
2023-03-09 18:05:53 tornado.access:INFO 200 GET /unsafe/filters:quality(60)/i.f1g.fr/media/cms/509x286_crop/2022/11/21/76bde3fc961f0fa8733756922d1e2ed06311d804ec38b89dc60d6ba36d30e046.jpg (10.201.2.1) 81.57ms
2023-03-09 18:05:53 thumbor:DEBUG METRICS: timing: response.time:80
2023-03-09 18:05:53 thumbor:DEBUG METRICS: timing: response.time.200:80
2023-03-09 18:05:53 thumbor:DEBUG METRICS: inc: response.status.200:1
2023-03-09 18:05:53 thumbor:DEBUG METRICS: inc: response.not_smart.count:1
2023-03-09 18:05:53 thumbor:DEBUG METRICS: timing: response.not_smart.latency:80
2023-03-09 18:05:53 thumbor:DEBUG METRICS: inc: response.format.jpg:1
2023-03-09 18:05:53 thumbor:DEBUG METRICS: timing: response.time.jpg:80
2023-03-09 18:05:53 thumbor:DEBUG METRICS: inc: response.bytes.jpg:31970
2023-03-09 18:05:53 thumbor:DEBUG [RESULT_STORAGE] putting at /data/thumbor/result_storage/default/16/10/fc6d87db0af8192db5a48d82b016d4c28918 (/data/thumbor/result_storage/default/16/10)
2023-03-09 18:05:53 thumbor:DEBUG METRICS: inc: result_storage.bytes_written:31970
2023-03-09 18:05:53 thumbor:DEBUG METRICS: timing: result_storage.outgoing_time:0
```

```
