@echo off
REM ###############################################################################
REM Frontend Setup Script for Windows
REM ===================================
REM This script automates the setup process for the React frontend on Windows.
REM 
REM Usage: setup.bat
REM ###############################################################################

echo =========================================
echo Fund Data Chatbot - Frontend Setup
echo =========================================
echo.

REM Check Node.js version
echo Checking Node.js version...
node --version
if %ERRORLEVEL% NEQ 0 (
    echo Error: Node.js is not installed
    echo Please install Node.js 18 or higher from https://nodejs.org/
    exit /b 1
)

REM Check npm
npm --version
if %ERRORLEVEL% NEQ 0 (
    echo Error: npm is not installed
    exit /b 1
)

REM Install dependencies
echo.
echo Installing dependencies...
npm install
echo Dependencies installed

REM Setup environment file
echo.
if not exist .env (
    echo Creating .env file from template...
    copy .env.example .env
    echo .env file created
) else (
    echo .env file already exists. Skipping...
)

echo.
echo =========================================
echo Frontend setup completed successfully!
echo =========================================
echo.
echo Next steps:
echo   1. Ensure backend is running on port 5000
echo   2. Run: npm run dev
echo   3. Open: http://localhost:3000
echo.
pause
