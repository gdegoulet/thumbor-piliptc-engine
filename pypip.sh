#!/bin/bash
v=$(fgrep __version__ thumbor_piliptc_engine/engine.py| cut -d"'" -f2)
rm -f dist/thumbor-piliptc-engine-${v}.tar.gz dist/thumbor-piliptc-engine-${v}-py3-none-any.whl
python3 -m build --sdist .
python3 -m build --wheel .
ls -al dist/
twine upload dist/thumbor_piliptc_engine-${v}.tar.gz dist/thumbor_piliptc_engine-${v}-py3-none-any.whl
