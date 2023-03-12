#!/bin/bash
docker run --rm -it -p8902:8000 \
  -e LOG_LEVEL=DEBUG \
  -e ENGINE=thumbor_piliptc_engine \
  -e PRESERVE_EXIF_INFO=True \
  -e FILE_LOADER_ROOT_PATH=/data/thumbor/tmp \
  -e FILE_STORAGE_ROOT_PATH=/data/thumbor/storage \
  -e RESULT_STORAGE_FILE_STORAGE_ROOT_PATH=/data/thumbor/result_storage \
  -e RESULT_STORAGE_STORES_UNSAFE=True \
  docker.io/gdegoulet/thumbor_piliptc_engine
