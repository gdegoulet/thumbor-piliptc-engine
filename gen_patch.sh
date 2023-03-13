#!/bin/bash
v=$1
test ! -f "thumbor/$v/pil.py" && echo "file not found thumbor/$v/pil.py" && exit 1
diff -Naur "thumbor/$v/pil.py" thumbor_piliptc_engine/engine.py > patch.txt
