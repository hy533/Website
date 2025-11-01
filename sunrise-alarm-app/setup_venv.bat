@echo off
REM Setup script for creating a clean virtual environment for Sunrise Alarm (Windows)

echo ================================================
echo   Sunrise Alarm Clock - Virtual Environment Setup
echo ================================================
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed.
    echo Please install Python 3.8+ from python.org
    pause
    exit /b 1
)

echo Found Python:
python --version
echo.

REM Create virtual environment
echo Creating virtual environment...
python -m venv sunrise_env

if errorlevel 1 (
    echo Failed to create virtual environment
    pause
    exit /b 1
)

echo Virtual environment created
echo.

REM Activate virtual environment
echo Activating virtual environment...
call sunrise_env\Scripts\activate.bat

if errorlevel 1 (
    echo Failed to activate virtual environment
    pause
    exit /b 1
)

echo Virtual environment activated
echo.

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

REM Install kivy
echo.
echo Installing Kivy (this may take a few minutes)...
pip install kivy

if errorlevel 1 (
    echo.
    echo Failed to install Kivy
    echo.
    echo If you're using Anaconda, try instead:
    echo   conda install -c conda-forge kivy
    pause
    exit /b 1
)

echo.
echo ================================================
echo   Setup Complete!
echo ================================================
echo.
echo To run the app:
echo.
echo   1. Activate the environment:
echo      sunrise_env\Scripts\activate
echo.
echo   2. Run the app:
echo      python main.py
echo.
echo   3. When done, deactivate:
echo      deactivate
echo.
echo Or use the quick launch script:
echo   run_venv.bat
echo.
echo ================================================
pause
