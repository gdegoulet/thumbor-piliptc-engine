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

```
ENGINE = "thumbor_piliptc_engine"
```

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
