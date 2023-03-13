#!/bin/bash
dir=$(dirname $(readlink -f $0))
release=$1
if test "$release" = ""
then
  release=$(curl --silent "https://api.github.com/repos/thumbor/thumbor/releases" | grep '"tag_name":' | sed -E 's/.*"([^"]+)".*/\1/' | head -n1)
fi
echo "release=$release dir=$dir"
test ! -d "$dir/thumbor/$release" && mkdir -p "$dir/thumbor/$release"
cd /tmp
rm -rf thumbor
git clone https://github.com/thumbor/thumbor.git
cd thumbor
git checkout $release
echo "copy thumbor/engines/pil.py $dir/thumbor/$release/"
cp thumbor/engines/pil.py "$dir/thumbor/$release/"
cd /tmp
rm -rf thumbor
cd "$dir"

