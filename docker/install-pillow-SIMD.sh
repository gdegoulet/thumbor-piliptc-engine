#!/bin/bash
set -eo pipefail

PILLOW_REPLACEMENT=pillow-simd

pip list
if test "$SIMD_LEVEL" != "no-cpu-optimization"
then
  echo
  echo "INSTALL ${PILLOW_REPLACEMENT} ( $SIMD_LEVEL )"
  pip list | grep -i pil || true
  pip uninstall -y pillow 
  pip list | grep -i pil || true
  LIB=/usr/lib/x86_64-linux-gnu/ INCLUDE=/usr/include/x86_64-linux-gnu/ CC="cc -m${SIMD_LEVEL}" pip install -v --no-cache-dir --prefix="${PYTHONUSERBASE}" -U --force-reinstall --no-binary=:all: --compile "${PILLOW_REPLACEMENT}>=${PILLOW_VERSION_MIN}" --global-option="build_ext" --global-option="--enable-lcms" --global-option="build_ext" --global-option="--enable-zlib" --global-option="build_ext" --global-option="--enable-jpeg" --global-option="build_ext" --global-option="--enable-tiff" | tee "${PYTHONUSERBASE}/pillow-simd.txt"
  echo
  pip list | grep -i pil || true
  echo
fi
