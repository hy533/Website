#!/bin/bash
# Quick run script using virtual environment

if [ ! -d "sunrise_env" ]; then
    echo "❌ Virtual environment not found!"
    echo ""
    echo "Please run setup first:"
    echo "  ./setup_venv.sh"
    echo ""
    exit 1
fi

echo "Starting Sunrise Alarm Clock..."
echo ""

# Activate and run
source sunrise_env/bin/activate
python main.py

# Deactivate when app closes
deactivate
