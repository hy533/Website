#!/bin/bash
# Setup script for creating a clean virtual environment for Sunrise Alarm

echo "================================================"
echo "  Sunrise Alarm Clock - Virtual Environment Setup"
echo "================================================"
echo ""

# Check Python version
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed."
    echo "Please install Python 3.8+ from python.org"
    exit 1
fi

echo "✓ Found Python: $(python3 --version)"
echo ""

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv sunrise_env

if [ $? -ne 0 ]; then
    echo "❌ Failed to create virtual environment"
    echo "Make sure you have python3-venv installed:"
    echo "  Ubuntu/Debian: sudo apt-get install python3-venv"
    echo "  Mac: Should be included with Python"
    exit 1
fi

echo "✓ Virtual environment created"
echo ""

# Activate virtual environment
echo "Activating virtual environment..."
source sunrise_env/bin/activate

if [ $? -ne 0 ]; then
    echo "❌ Failed to activate virtual environment"
    exit 1
fi

echo "✓ Virtual environment activated"
echo ""

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install kivy
echo ""
echo "Installing Kivy (this may take a few minutes)..."
pip install kivy

if [ $? -ne 0 ]; then
    echo ""
    echo "❌ Failed to install Kivy"
    echo ""
    echo "If you're using Anaconda, try instead:"
    echo "  conda install -c conda-forge kivy"
    exit 1
fi

echo ""
echo "================================================"
echo "  ✓ Setup Complete!"
echo "================================================"
echo ""
echo "To run the app:"
echo ""
echo "  1. Activate the environment:"
echo "     source sunrise_env/bin/activate"
echo ""
echo "  2. Run the app:"
echo "     python main.py"
echo ""
echo "  3. When done, deactivate:"
echo "     deactivate"
echo ""
echo "Or use the quick launch script:"
echo "  ./run_venv.sh"
echo ""
echo "================================================"
