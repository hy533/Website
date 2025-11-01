#!/bin/bash
# Quick run script for Sunrise Alarm Clock

echo "======================================="
echo "  Sunrise Alarm Clock"
echo "======================================="
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed."
    echo "Please install Python 3.8 or higher from python.org"
    exit 1
fi

echo "Python version:"
python3 --version
echo ""

# Check if kivy is installed
if ! python3 -c "import kivy" 2>/dev/null; then
    echo "Kivy is not installed. Installing dependencies..."
    echo ""
    pip3 install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo ""
        echo "Error: Failed to install dependencies."
        echo "Please run: pip3 install -r requirements.txt"
        exit 1
    fi
    echo ""
    echo "Dependencies installed successfully!"
    echo ""
fi

echo "Starting Sunrise Alarm Clock..."
echo ""
echo "Tips:"
echo "  - Press ESC or Cmd+Q to quit"
echo "  - Use 'Test Sunrise' button for a quick demo"
echo "  - Add alarms and configure weekly routines"
echo ""
echo "======================================="
echo ""

# Run the application
python3 main.py
