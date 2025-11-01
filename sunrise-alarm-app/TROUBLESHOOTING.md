# Troubleshooting Installation Issues

## Issue: Anaconda/Conda Environment Conflicts

If you see errors like:
```
InvalidVersion: Invalid version: '4.0.0-unsupported'
```

This happens when existing packages in your Anaconda environment have non-standard version numbers that conflict with pip.

## Solutions (Try in Order)

### Solution 1: Use Conda to Install Kivy (Recommended for Anaconda Users)

```bash
# Use conda instead of pip
conda install -c conda-forge kivy

# If that works, run the app
python main.py
```

### Solution 2: Create a Clean Virtual Environment

This is the **best solution** to avoid conflicts:

#### Using venv (Built-in Python):

```bash
# Navigate to app directory
cd sunrise-alarm-app

# Create virtual environment
python3 -m venv sunrise_env

# Activate it:
# On Mac/Linux:
source sunrise_env/bin/activate
# On Windows:
sunrise_env\Scripts\activate

# Install kivy in clean environment
pip install kivy

# Run the app
python main.py

# When done, deactivate:
deactivate
```

#### Using Conda:

```bash
# Create new conda environment
conda create -n sunrise python=3.9

# Activate it
conda activate sunrise

# Install kivy
conda install -c conda-forge kivy

# Run the app
python main.py

# When done:
conda deactivate
```

### Solution 3: Update Pip and Try Again

```bash
# Update pip to latest version
python -m pip install --upgrade pip

# Try installing kivy again
pip install kivy --ignore-installed
```

### Solution 4: Install Without Dependencies Check

```bash
# Skip checking other package versions
pip install kivy --no-deps

# Then install kivy's dependencies manually if needed
pip install Kivy-Garden docutils pygments requests filetype
```

### Solution 5: Fix the Problematic Package

```bash
# Reinstall the problematic package
conda remove pyodbc
conda install -c conda-forge pyodbc

# Or skip it if you don't need it
# Then try installing kivy again
pip install kivy
```

## Which Solution Should I Use?

**If you have Anaconda/Conda installed:**
- ✅ **Best: Solution 1** (Use conda to install kivy)
- ✅ **Also Good: Solution 2 with Conda** (Create clean environment)

**If you have standard Python:**
- ✅ **Best: Solution 2 with venv** (Create clean environment)

**Quick and dirty (not recommended):**
- ⚠️ Solution 4 (May cause issues later)

## After Installation Success

Once kivy is installed, test the app:

```bash
python main.py
```

You should see the Sunrise Alarm Clock window open!

## Other Common Issues

### "Python not found"

Make sure Python is installed:
```bash
python --version
# or
python3 --version
```

Should show Python 3.8 or higher.

### "Cannot find main.py"

Make sure you're in the right directory:
```bash
cd /path/to/sunrise-alarm-app
ls main.py
```

### App Window Won't Open

This might happen if you're running headless (no display). Make sure you're on a computer with a GUI display.

### Permission Errors

On Mac/Linux, don't use `sudo pip install`. Instead use a virtual environment.

## Still Having Issues?

1. **Check Python version**: `python --version` (needs 3.8+)
2. **Check if display available**: `echo $DISPLAY` (Mac/Linux)
3. **Try the virtual environment method** (most reliable)
4. **Check the error message carefully** and search for the specific error

## Contact / Resources

- Kivy Documentation: https://kivy.org/doc/stable/
- Kivy Installation Guide: https://kivy.org/doc/stable/gettingstarted/installation.html
- Conda Kivy Package: https://anaconda.org/conda-forge/kivy
