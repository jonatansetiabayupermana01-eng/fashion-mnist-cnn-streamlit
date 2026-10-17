#!/usr/bin/env bash
# Setup + jalankan aplikasi (Linux/macOS).
set -e
cd "$(dirname "$0")"

# NixOS
if [ -e /etc/NIXOS ] && [ -z "$IN_NIX_SHELL" ]; then
  exec nix-shell shell.nix --run "bash run.sh"
fi

PY=""
for c in python3.12 python3.11 python3.13 python3.10 python3; do
  if command -v "$c" >/dev/null 2>&1; then
    v=$("$c" -c 'import sys;print(sys.version_info[0]*100+sys.version_info[1])')
    if [ "$v" -ge 310 ] && [ "$v" -le 313 ]; then PY="$c"; break; fi
  fi
done
if [ -z "$PY" ]; then
  # Tidak ada Python 3.10-3.13: unduh Python 3.12
  echo "Python 3.10-3.13 tidak ditemukan. Mengunduh Python 3.12 lewat uv..."
  if ! command -v uv >/dev/null 2>&1; then
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.local/bin:$PATH"
  fi
  uv python install 3.12
  PY="$(uv python find 3.12)"
fi
echo "Memakai $($PY --version)"

if [ ! -d .venv ]; then "$PY" -m venv .venv; fi
. .venv/bin/activate
python -m pip install --upgrade pip -q
python -m pip install -r requirements.txt
python -m streamlit run app.py
