@echo off
REM Quick run script for Sunrise Alarm Clock (Windows)

echo =======================================
echo   Sunrise Alarm Clock
echo =======================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed.
    echo Please install Python 3.8 or higher from python.org
    pause
    exit /b 1
)

echo Python version:
python --version
echo.

REM Check if kivy is installed
python -c "import kivy" >nul 2>&1
if errorlevel 1 (
    echo Kivy is not installed. Installing dependencies...
    echo.
    pip install -r requirements.txt
    if errorlevel 1 (
        echo.
        echo Error: Failed to install dependencies.
        echo Please run: pip install -r requirements.txt
        pause
        exit /b 1
    )
    echo.
    echo Dependencies installed successfully!
    echo.
)

echo Starting Sunrise Alarm Clock...
echo.
echo Tips:
echo   - Press ESC to quit
echo   - Use 'Test Sunrise' button for a quick demo
echo   - Add alarms and configure weekly routines
echo.
echo =======================================
echo.

REM Run the application
python main.py
