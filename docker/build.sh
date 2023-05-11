#!/bin/bash
cd $(dirname $(readlink -f $0))
test ! -f ../thumbor_piliptc_engine/engine.py && exit 1
THUMBOR_VERSION=$(fgrep __version__ ../thumbor_piliptc_engine/engine.py |cut -d "'" -f2 | cut -d '.' -f1-3)
echo "building $THUMBOR_VERSION"
docker build --no-cache --pull -t docker.io/gdegoulet/thumbor_piliptc_engine:${THUMBOR_VERSION}-avx2 --build-arg THUMBOR_VERSION=$THUMBOR_VERSION --build-arg BUILD_DATE=$(date -u +'%Y-%m-%dT%H:%M:%SZ') --build-arg SIMD_LEVEL=avx2 .
test $? -ne 0 && exit 1
docker build --no-cache --pull -t docker.io/gdegoulet/thumbor_piliptc_engine:${THUMBOR_VERSION}-sse4 --build-arg THUMBOR_VERSION=$THUMBOR_VERSION --build-arg BUILD_DATE=$(date -u +'%Y-%m-%dT%H:%M:%SZ') --build-arg SIMD_LEVEL=sse4 .
test $? -ne 0 && exit 1
docker build --no-cache --pull -t docker.io/gdegoulet/thumbor_piliptc_engine:${THUMBOR_VERSION}      --build-arg THUMBOR_VERSION=$THUMBOR_VERSION --build-arg BUILD_DATE=$(date -u +'%Y-%m-%dT%H:%M:%SZ') .
test $? -ne 0 && exit 1
docker tag docker.io/gdegoulet/thumbor_piliptc_engine:${THUMBOR_VERSION} docker.io/gdegoulet/thumbor_piliptc_engine:latest
test $? -ne 0 && exit 1

echo gdegoulet/thumbor_piliptc_engine:${THUMBOR_VERSION}
docker run --rm -it docker.io/gdegoulet/thumbor_piliptc_engine:${THUMBOR_VERSION}      pip list | egrep -i "(thumbor|iptc|jpeg|pillow)"
test $? -ne 0 && exit 1
echo gdegoulet/thumbor_piliptc_engine:${THUMBOR_VERSION}-sse4
docker run --rm -it docker.io/gdegoulet/thumbor_piliptc_engine:${THUMBOR_VERSION}-sse4 pip list | egrep -i "(thumbor|iptc|jpeg|pillow)"
test $? -ne 0 && exit 1
echo gdegoulet/thumbor_piliptc_engine:${THUMBOR_VERSION}-avx2
docker run --rm -it docker.io/gdegoulet/thumbor_piliptc_engine:${THUMBOR_VERSION}-avx2 pip list | egrep -i "(thumbor|iptc|jpeg|pillow)"
test $? -ne 0 && exit 1

exit 0
