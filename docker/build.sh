#!/bin/bash
cd $(dirname $(readlink -f $0))
test ! -f ../thumbor_piliptc_engine/engine.py && exit 1
THUMBOR_VERSION=$(fgrep __version__ ../thumbor_piliptc_engine/engine.py |cut -d "'" -f2 | cut -d '.' -f1-3)
echo "building $THUMBOR_VERSION"
docker build -t gdegoulet/thumbor_piliptc_engine:${THUMBOR_VERSION}-sse4 --build-arg THUMBOR_VERSION=$THUMBOR_VERSION --build-arg BUILD_DATE=$(date +%Y%m%d%H%M) --build-arg SIMD_LEVEL=sse4 .
docker build -t gdegoulet/thumbor_piliptc_engine:${THUMBOR_VERSION}      --build-arg THUMBOR_VERSION=$THUMBOR_VERSION --build-arg BUILD_DATE=$(date +%Y%m%d%H%M) .
docker tag gdegoulet/thumbor_piliptc_engine:${THUMBOR_VERSION} gdegoulet/thumbor_piliptc_engine:latest

echo gdegoulet/thumbor_piliptc_engine:${THUMBOR_VERSION}
docker run --rm -it gdegoulet/thumbor_piliptc_engine:${THUMBOR_VERSION}      pip list | egrep -i "(thumbor|iptc|jpeg|pillow)"
echo gdegoulet/thumbor_piliptc_engine:${THUMBOR_VERSION}-sse4
docker run --rm -it gdegoulet/thumbor_piliptc_engine:${THUMBOR_VERSION}-sse4 pip list | egrep -i "(thumbor|iptc|jpeg|pillow)"


