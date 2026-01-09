@echo off
REM ###############################################################################
REM Backend Setup Script for Windows
REM ==================================
REM This script automates the setup process for the backend server on Windows.
REM 
REM Usage: setup.bat
REM ###############################################################################

echo =========================================
echo Fund Data Chatbot - Backend Setup
echo =========================================
echo.

REM Check Python version
echo Checking Python version...
python --version
if %ERRORLEVEL% NEQ 0 (
    echo Error: Python is not installed or not in PATH
    exit /b 1
)

REM Create virtual environment
echo.
echo Creating virtual environment...
if exist venv (
    echo Virtual environment already exists. Skipping...
) else (
    python -m venv venv
    echo Virtual environment created
)

REM Activate virtual environment
echo.
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Upgrade pip
echo.
echo Upgrading pip...
python -m pip install --upgrade pip

REM Install dependencies
echo.
echo Installing dependencies...
pip install -r requirements.txt
echo Dependencies installed

REM Setup environment file
echo.
if not exist .env (
    echo Creating .env file from template...
    copy .env.example .env
    echo .env file created
    echo.
    echo WARNING: Please edit .env file and add your API keys!
    echo.
    echo Required API keys:
    echo   - OPENAI_API_KEY (https://platform.openai.com/api-keys^)
    echo   - GEMINI_API_KEY (https://makersuite.google.com/app/apikey^)
    echo   - ANTHROPIC_API_KEY (https://console.anthropic.com/^)
) else (
    echo .env file already exists. Skipping...
)

echo.
echo =========================================
echo Backend setup completed successfully!
echo =========================================
echo.
echo Next steps:
echo   1. Edit backend\.env and add your API keys
echo   2. Run: venv\Scripts\activate.bat
echo   3. Run: python app.py
echo.
pause
