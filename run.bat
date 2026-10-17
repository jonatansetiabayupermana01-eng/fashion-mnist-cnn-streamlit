@echo off
REM Setup + jalankan aplikasi (Windows). Pemakaian: run.bat
cd /d "%~dp0"

set PY=
for %%V in (3.12 3.11 3.13 3.10) do (
  if not defined PY (
    py -%%V -c "import sys" >nul 2>&1 && set PY=py -%%V
  )
)
if not defined PY (
  echo Butuh Python 3.10 sampai 3.13. Install dari https://www.python.org/downloads/ lalu jalankan ulang.
  pause
  exit /b 1
)
echo Memakai %PY%

if not exist .venv %PY% -m venv .venv
call .venv\Scripts\activate.bat
python -m pip install --upgrade pip -q
python -m pip install -r requirements.txt
python -m streamlit run app.py
