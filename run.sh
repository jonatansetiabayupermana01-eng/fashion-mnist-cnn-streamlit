#!/usr/bin/env bash
# Setup + jalankan aplikasi (Linux/macOS). Pemakaian: bash run.sh
set -e
cd "$(dirname "$0")"

PY=""
for c in python3.12 python3.11 python3.13 python3.10 python3; do
  if command -v "$c" >/dev/null 2>&1; then
    v=$("$c" -c 'import sys;print(sys.version_info[0]*100+sys.version_info[1])')
    if [ "$v" -ge 310 ] && [ "$v" -le 313 ]; then PY="$c"; break; fi
  fi
done
if [ -z "$PY" ]; then
  echo "Butuh Python 3.10 sampai 3.13 (TensorFlow belum mendukung versi lain). Install dari https://www.python.org/downloads/"
  exit 1
fi
echo "Memakai $($PY --version)"

if [ ! -d .venv ]; then "$PY" -m venv .venv; fi
. .venv/bin/activate
python -m pip install --upgrade pip -q
python -m pip install -r requirements.txt
python -m streamlit run app.py
