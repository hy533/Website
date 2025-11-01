@echo off
REM Quick run script using virtual environment (Windows)

if not exist "sunrise_env\" (
    echo Virtual environment not found!
    echo.
    echo Please run setup first:
    echo   setup_venv.bat
    echo.
    pause
    exit /b 1
)

echo Starting Sunrise Alarm Clock...
echo.

REM Activate and run
call sunrise_env\Scripts\activate.bat
python main.py

REM Deactivate when app closes
deactivate
