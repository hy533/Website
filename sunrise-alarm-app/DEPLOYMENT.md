# Detailed iPad Deployment Guide

This guide provides comprehensive instructions for deploying the Sunrise Alarm app to your iPad.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Method 1: Kivy-iOS (Recommended)](#method-1-kivy-ios-recommended)
3. [Method 2: Alternative Approaches](#method-2-alternative-approaches)
4. [Troubleshooting](#troubleshooting)
5. [Development Tips](#development-tips)

## Prerequisites

### For All Methods

- **Python 3.8 or higher** installed on your computer
- **iPad** running iPadOS 12.0 or later
- **USB cable** to connect iPad to computer

### For Native iOS Build (Method 1)

- **Mac computer** running macOS 10.14 or later
- **Xcode 12 or later** (free from Mac App Store)
- **Apple Developer Account** (free tier is sufficient)
- **Homebrew** package manager for macOS
- **8GB+ free disk space** for build tools
- **At least 1 hour** for initial setup

## Method 1: Kivy-iOS (Recommended)

This method creates a native iOS app that runs directly on your iPad.

### Step 1: Install Xcode and Command Line Tools

1. **Install Xcode:**
   ```bash
   # Install from Mac App Store or:
   xcode-select --install
   ```

2. **Accept Xcode license:**
   ```bash
   sudo xcodebuild -license accept
   ```

3. **Verify installation:**
   ```bash
   xcode-select -p
   # Should output: /Applications/Xcode.app/Contents/Developer
   ```

### Step 2: Install Homebrew (if not already installed)

```bash
# Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Verify installation
brew --version
```

### Step 3: Install Required Dependencies

```bash
# Install system dependencies
brew install autoconf automake libtool pkg-config

# Install SDL2 libraries (required for Kivy on iOS)
brew install sdl2 sdl2_image sdl2_mixer sdl2_ttf

# Install Python 3 if needed
brew install python3

# Install Cython (specific version for compatibility)
pip3 install Cython==0.29.36
```

### Step 4: Download and Setup Kivy-iOS

```bash
# Create a workspace directory
mkdir ~/kivy-projects
cd ~/kivy-projects

# Clone kivy-ios repository
git clone https://github.com/kivy/kivy-ios.git
cd kivy-ios

# Verify toolchain is working
python3 toolchain.py --help
```

### Step 5: Build Python and Kivy for iOS

This step compiles Python and Kivy to work on iOS devices. It takes time but only needs to be done once.

```bash
# Build Python 3 for iOS (15-20 minutes)
python3 toolchain.py build python3

# Build Kivy (20-30 minutes)
python3 toolchain.py build kivy

# If you encounter errors, clean and retry:
python3 toolchain.py clean kivy
python3 toolchain.py build kivy
```

### Step 6: Create Xcode Project

```bash
# Navigate to kivy-ios directory
cd ~/kivy-projects/kivy-ios

# Create Xcode project for your app
# Replace /path/to/sunrise-alarm-app with actual path
python3 toolchain.py create SunriseAlarm /path/to/sunrise-alarm-app

# This creates a folder: SunriseAlarm-ios/
```

### Step 7: Configure Xcode Project

1. **Open the project:**
   ```bash
   open SunriseAlarm-ios/SunriseAlarm.xcodeproj
   ```

2. **In Xcode:**
   - Click on "SunriseAlarm" in the left sidebar (top of project navigator)
   - Select the "SunriseAlarm" target
   - Go to "Signing & Capabilities" tab

3. **Setup signing:**
   - Check "Automatically manage signing"
   - Select your Team (sign in with Apple ID if needed)
   - Bundle Identifier: Change to something unique like `com.yourname.sunrisealarm`

4. **Configure deployment:**
   - In "General" tab, set "Deployment Target" to iOS 12.0 or higher
   - Set "Devices" to "iPad" (or Universal for both iPhone/iPad)

### Step 8: Deploy to iPad

1. **Connect iPad:**
   - Connect iPad to Mac via USB
   - Unlock iPad and tap "Trust This Computer" if prompted

2. **Select device:**
   - In Xcode, click the device selector (top left, near Play button)
   - Select your iPad from the list

3. **Build and run:**
   - Click the "Play" button (▶️) or press Cmd+R
   - Xcode will compile and install the app
   - First build may take 5-10 minutes

4. **Trust developer certificate (first time only):**
   - On iPad: Settings > General > VPN & Device Management
   - Find your Apple ID under "Developer App"
   - Tap and select "Trust"
   - Return to home screen and launch the app

### Step 9: Verify Installation

- App icon should appear on iPad home screen
- Launch the app
- Test basic functionality:
  - Add an alarm
  - Use "Test Sunrise" button
  - Check settings

## Method 2: Alternative Approaches

### Option A: Using Pythonista (Easier but Limited)

Pythonista is a paid iOS app that runs Python code directly on iPad.

1. **Purchase Pythonista:**
   - App Store: https://apps.apple.com/app/pythonista-3/id1085978097
   - Cost: ~$10 USD

2. **Transfer code:**
   - Open Pythonista on iPad
   - Create new file named `sunrise_alarm.py`
   - Copy entire contents of `main.py` into it

3. **Limitations:**
   - Kivy may not work in Pythonista without modifications
   - You might need to use Pythonista's UI framework instead
   - Full screen mode may be limited

### Option B: Remote Desktop

Run the app on your Mac/PC and display it on iPad:

1. **Install VNC server on computer:**
   ```bash
   # macOS: Use built-in Screen Sharing
   # Or install RealVNC, TightVNC, etc.
   ```

2. **Install VNC client on iPad:**
   - Download "VNC Viewer" from App Store

3. **Run app on computer:**
   ```bash
   cd sunrise-alarm-app
   python3 main.py
   ```

4. **Connect from iPad:**
   - Open VNC Viewer
   - Connect to your computer's IP
   - View and interact with the app

**Pros:** Easy setup, no iOS build required
**Cons:** Requires computer to be running, network connection needed

### Option C: Using iPad Web Browser

Convert the app to a web application:

1. **Use Kivy's web backend** (experimental):
   ```bash
   pip install kivy-garden
   garden install webview
   ```

2. **Or rebuild using web framework:**
   - Convert to Flask/Django web app
   - Use HTML5/CSS3 for UI
   - Run server on computer or cloud
   - Access from iPad Safari in full-screen mode

## Troubleshooting

### Kivy-iOS Build Errors

**Error: "Command failed: python3 toolchain.py build kivy"**

Solution:
```bash
# Clean and rebuild
python3 toolchain.py clean kivy
python3 toolchain.py clean python3

# Ensure Cython version is correct
pip3 uninstall Cython
pip3 install Cython==0.29.36

# Rebuild
python3 toolchain.py build python3
python3 toolchain.py build kivy
```

**Error: "No such file or directory: 'xcrun'"**

Solution:
```bash
# Install Xcode Command Line Tools
xcode-select --install

# Reset Xcode path
sudo xcode-select --reset
```

**Error: "SDK not found"**

Solution:
```bash
# Check available SDKs
xcodebuild -showsdks

# Update kivy-ios to latest version
cd ~/kivy-projects/kivy-ios
git pull origin master
```

### Xcode Signing Errors

**Error: "Failed to create provisioning profile"**

Solution:
1. Open Xcode preferences (Cmd+,)
2. Go to "Accounts" tab
3. Remove and re-add your Apple ID
4. Download manual provisioning profiles

**Error: "Team has not been found"**

Solution:
1. Sign in to https://developer.apple.com
2. Accept any pending agreements
3. Return to Xcode and re-select team

### Runtime Errors on iPad

**App crashes on launch:**

Check crash logs:
1. Xcode > Window > Devices and Simulators
2. Select your iPad
3. View Device Logs
4. Look for SunriseAlarm crash logs

Common fixes:
```bash
# Ensure all dependencies are included in Xcode project
# Add to buildozer.spec requirements:
requirements = python3,kivy,ios

# Rebuild project
python3 toolchain.py create SunriseAlarm /path/to/app --force
```

**App doesn't fill screen:**

Add to main.py:
```python
from kivy.config import Config
Config.set('graphics', 'fullscreen', 'auto')
Config.set('graphics', 'window_state', 'maximized')
```

### Performance Issues

If app runs slowly on iPad:

1. **Reduce animation frequency:**
   ```python
   # In main.py, change update interval
   Clock.schedule_interval(self.update_sunrise, 2)  # Every 2 seconds instead of 1
   ```

2. **Optimize graphics:**
   ```python
   from kivy.config import Config
   Config.set('graphics', 'multisamples', '0')
   ```

3. **Enable app-specific optimizations:**
   ```python
   Config.set('kivy', 'log_level', 'warning')  # Reduce logging
   ```

## Development Tips

### Testing on Simulator

Before deploying to real iPad, test on simulator:

```bash
# Install iOS simulator support
python3 toolchain.py build kivy --arch x86_64

# Create simulator build
python3 toolchain.py create SunriseAlarm /path/to/app --simulator

# Open in Xcode and select a simulator device
```

### Debugging

Enable debug mode in main.py:

```python
# Add at top of file
import logging
logging.basicConfig(level=logging.DEBUG)

# Add debug prints throughout code
print(f"Alarm triggered: {alarm}")
```

View logs in Xcode:
- Run app from Xcode
- View output in bottom console panel
- Use print statements for debugging

### Updating the App

After making changes to code:

1. **Save changes** to main.py

2. **Rebuild in Xcode:**
   - Just click Run again
   - Xcode will copy updated main.py
   - App will reinstall on iPad

3. **For major changes:**
   ```bash
   # Recreate Xcode project
   python3 toolchain.py create SunriseAlarm /path/to/app --force
   ```

### Distribution

To share app with others:

1. **Ad-Hoc Distribution:**
   - Requires paid Apple Developer account ($99/year)
   - Can distribute to up to 100 devices
   - Uses TestFlight

2. **App Store:**
   - Requires paid Developer account
   - Submit for review
   - Available to public

For personal use, free developer account is sufficient.

## Additional Resources

- **Kivy Documentation:** https://kivy.org/doc/stable/
- **Kivy-iOS GitHub:** https://github.com/kivy/kivy-ios
- **Kivy Discord:** https://chat.kivy.org/
- **Apple Developer:** https://developer.apple.com/
- **Xcode Help:** https://developer.apple.com/documentation/xcode

## Need Help?

1. Check error messages carefully
2. Search Kivy-iOS GitHub issues
3. Review Kivy documentation
4. Ask on Kivy community forums

Remember: Initial setup takes time, but once configured, updates are quick and easy!
