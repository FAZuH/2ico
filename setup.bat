@echo off
color 5

title Checking Python Version
python --version 2>&1 | findstr "3.11."
if %errorlevel%==0 (
    echo Python 3.11.0 or higher is already installed
) else (
    echo Python 3.11.0 or higher is not installed
    echo Please install Python 3.11.0 or higher and add it to your PATH
    timeout /t 5 >nul
)

title Installing Requirements
cd /d "%~dp0"

if not exist .venv (
    python -m venv .venv
    call .venv\Scripts\activate
    echo Installing Requirements...
    python -m pip install -r requirements.txt
    call .venv\Scripts\deactivate
) else (
    echo Virtual environment (.venv) already exists. Skipping installation.
)

title Creating IO Directories
echo Creating IO Directories...
mkdir input_image
mkdir output_ico
mkdir output_image
