# Build
FROM python:3.11-slim-bullseye as build

ENV \
  DEBIAN_FRONTEND=noninteractive \
  PATH=$PATH:/app/bin/ \
  PYTHONUSERBASE=/app \
  PYTHONPATH=/app/lib/python3.11/site-packages \
  PILLOW_VERSION_MIN=9.0.0

ENV VERSION_graphicsmagick=1.4+really1.3.36+hg16481-2+deb11u1
ENV VERSION_ffmpeg=7:4.3.5-0+deb11u1

ARG THUMBOR_VERSION=7.4.7
ARG SIMD_LEVEL=no-cpu-optimization
COPY install-pillow-SIMD.sh /install-pillow-SIMD.sh

RUN mkdir "$PYTHONUSERBASE" /etc/thumbor \
 && apt-get update > /dev/null \
 && apt-get install -y -qq --no-install-recommends \
    build-essential=12.9 \
    ca-certificates=20210119 \
    cairosvg=2.5.0-1.1 \
    ffmpeg=${VERSION_ffmpeg} \
    graphicsmagick=${VERSION_graphicsmagick} \
    libboost-python-dev=1.74.0.3 \
    libcurl4-openssl-dev \
    libgraphicsmagick++1-dev=${VERSION_graphicsmagick} \
    libjpeg62-turbo-dev \
    libturbojpeg0-dev \
    libopencv-dev=4.5.1+dfsg-5 \
    libpng-dev=1.6.37-3 \
    libssl-dev \
    libtiff5-dev=4.2.0-1+deb11u1 \
    webp=0.6.1-2.1 \
    git \
    > /dev/null \
 && python -m pip install --upgrade pip \
 && pip install \
    --no-cache-dir \
    --prefix="${PYTHONUSERBASE}" \
      envtpl==0.7.2 \
      cairosvg==2.6.0 \
      numpy==1.24.2 \
      opencv-python-headless==4.7.0.72 \
      pillow>=$PILLOW_VERSION_MIN \
      pycurl==7.45.2 \
      piexif==1.1.3 \
      remotecv==5.1.1 \
      tc_prometheus==2.0.0 \
      tc-mongodb==5.1.0 \
      tc-redis==2.3.0 \
      tc-shortener==0.2.2 \
      tc-aws==7.0.2 \
      thumbor-plugins-gifv==0.1.2 \
      thumbor-plugins==0.2.4 \
      thumbor=="${THUMBOR_VERSION}" \
      git+https://github.com/gdegoulet/thumbor-piliptc-engine@v1.1.0 \
 && chmod +x /install-pillow-SIMD.sh \
 && /install-pillow-SIMD.sh \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Run
FROM python:3.11-slim-bullseye

ENV \
  DEBIAN_FRONTEND=noninteractive \
  PYTHONUSERBASE=/app \
  PYTHONPATH=/app/lib/python3.11/site-packages \
  PATH=$PATH:/app/bin/ \
  THUMBOR_PORT=8000 \
  LOG_LEVEL=

ENV VERSION_graphicsmagick=1.4+really1.3.36+hg16481-2+deb11u1
ENV VERSION_ffmpeg=7:4.3.5-0+deb11u1

ARG BUILD_DATE
ARG SIMD_LEVEL=no-cpu-optimization
ARG THUMBOR_VERSION=7.4.7

LABEL maintainer="docker@degoulet.net" \
  org.label-schema.build-date="$BUILD_DATE" \
  org.label-schema.name="thumbor" \
  org.label-schema.schema-version="1.0" \
  org.label-schema.vendor="thumbor" \
  org.label-schema.version="$THUMBOR_VERSION" \
  org.label-schema.simd_level="$SIMD_LEVEL" \
  org.opencontainers.image.created="$BUILD_DATE" \
  org.opencontainers.image.title="thumbor" \
  org.opencontainers.image.vendor="thumbor" \
  org.opencontainers.image.version="$THUMBOR_VERSION" \
  org.opencontainers.image.simd_level="$SIMD_LEVEL"

COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN groupadd -g 301 ftponly \
 && useradd -u 201 -d /home/vdx -ms /bin/bash -g ftponly vdx \
 && apt-get update > /dev/null \
 && apt-get install -y -qq --no-install-recommends \
    ca-certificates=20210119 \
    cairosvg=2.5.0-1.1 \
    ffmpeg=${VERSION_ffmpeg} \
    gifsicle=1.92-2+b1 \
    graphicsmagick=${VERSION_graphicsmagick} \
    libjpeg-turbo-progs=1:2.0.6-4 \
    libjpeg62-turbo \
    libturbojpeg0 \
    libcurl4 \
    webp=0.6.1-2.1 \
    curl wget procps \
    > /dev/null \
 && mkdir /usr/src/app \
 && chmod 1777 /usr/src/app \
 && ln -s /usr/src/app /etc/thumbor \
 && chmod +x /docker-entrypoint.sh \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

COPY --from=build "$PYTHONUSERBASE" "$PYTHONUSERBASE"
COPY thumbor.conf.tpl /usr/src/app/thumbor.conf.tpl

VOLUME /data

EXPOSE 8000/tcp

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["thumbor"]
