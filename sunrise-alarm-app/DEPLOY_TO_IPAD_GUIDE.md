# Step-by-Step: Deploy Sunrise Alarm to Your iPad

This guide will walk you through deploying the app to your iPad for testing.

## ⚡ Quick Overview

**Time needed**: 60-90 minutes (first time only)
**What you need**: Mac computer, iPad, USB cable
**Cost**: Free (using free Apple Developer account)

---

## Step 1: Prerequisites ✅

### Do you have these?

- [ ] **Mac computer** (macOS 10.14 or later)
- [ ] **iPad** (iPadOS 12.0 or later)
- [ ] **USB cable** to connect iPad to Mac
- [ ] **Xcode** installed (free from Mac App Store)
- [ ] **Apple ID** (free, no paid developer account needed)
- [ ] **8GB free disk space**

### Install Xcode (if not already installed)

1. Open **Mac App Store**
2. Search for **"Xcode"**
3. Click **Get** (it's large, ~12GB - will take time)
4. Wait for download and installation

After Xcode installs, open **Terminal** and run:
```bash
# Accept Xcode license
sudo xcodebuild -license accept

# Install command line tools
xcode-select --install

# Verify installation
xcode-select -p
# Should output: /Applications/Xcode.app/Contents/Developer
```

---

## Step 2: Install Build Dependencies 🔧

Open **Terminal** and run these commands one by one:

### 2.1 Install Homebrew (if you don't have it)

```bash
# Check if you have Homebrew
brew --version

# If not, install it:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 2.2 Install Required Tools

```bash
# Install build tools
brew install autoconf automake libtool pkg-config

# Install SDL2 libraries (required for Kivy on iOS)
brew install sdl2 sdl2_image sdl2_mixer sdl2_ttf

# Install specific Cython version
pip3 install Cython==0.29.36
```

**Expected time**: 10-15 minutes

---

## Step 3: Setup Kivy-iOS Toolchain 📦

This is the tool that converts Python/Kivy apps to iOS apps.

### 3.1 Download Kivy-iOS

```bash
# Create a workspace
mkdir ~/kivy-projects
cd ~/kivy-projects

# Clone kivy-ios
git clone https://github.com/kivy/kivy-ios.git
cd kivy-ios

# Verify it works
python3 toolchain.py --help
```

You should see help text about the toolchain.

---

## Step 4: Build iOS Libraries ⚙️

This step compiles Python and Kivy to work on iOS. **This takes time but only needs to be done once!**

### 4.1 Build Python for iOS

```bash
cd ~/kivy-projects/kivy-ios

# Build Python (15-20 minutes)
python3 toolchain.py build python3
```

**What you'll see**: Lots of compilation output. Don't worry if you see warnings - errors will stop the process.

### 4.2 Build Kivy for iOS

```bash
# Build Kivy (20-30 minutes)
python3 toolchain.py build kivy
```

**Troubleshooting**: If you get errors:
```bash
# Clean and retry
python3 toolchain.py clean kivy
python3 toolchain.py build kivy
```

**Total expected time**: 30-60 minutes (grab a coffee! ☕)

---

## Step 5: Create Your App's Xcode Project 📱

Now we'll create an Xcode project specifically for your Sunrise Alarm app.

### 5.1 Find Your App Path

First, find where your app is located:
```bash
cd ~/Website/sunrise-alarm-app
pwd
```

Copy this path (you'll need it in the next step).

### 5.2 Create Xcode Project

```bash
cd ~/kivy-projects/kivy-ios

# Create project (replace /path/to/app with your actual path)
python3 toolchain.py create SunriseAlarm /path/to/your/Website/sunrise-alarm-app

# Example:
# python3 toolchain.py create SunriseAlarm /Users/yourname/Website/sunrise-alarm-app
```

This creates a folder called `SunriseAlarm-ios/`

### 5.3 Open in Xcode

```bash
open SunriseAlarm-ios/SunriseAlarm.xcodeproj
```

Xcode should open with your project!

---

## Step 6: Configure Xcode for iPad 🎨

Now we need to configure Xcode to deploy to your iPad.

### 6.1 Sign In to Xcode

1. Open **Xcode Preferences** (Cmd + ,)
2. Go to **Accounts** tab
3. Click **+** and select **Apple ID**
4. Sign in with your Apple ID
5. Wait for authentication

### 6.2 Configure Project Settings

In Xcode's main window:

1. **Select the project** in left sidebar (top item, blue icon)
2. Select **"SunriseAlarm" target** in the main area
3. Go to **"Signing & Capabilities"** tab

4. **Enable signing**:
   - ✅ Check "Automatically manage signing"
   - Under **Team**: Select your Apple ID / Personal Team

5. **Set Bundle Identifier** (must be unique):
   - Change `org.test.sunrisealarm` to something like:
   - `com.yourname.sunrisealarm` (replace `yourname` with your actual name)

6. **Set Deployment Target**:
   - Go to **General** tab
   - Find "Deployment Info"
   - Set **Deployment Target** to iOS 12.0 or higher
   - Under **Devices**: Select **iPad** (or Universal)

---

## Step 7: Connect iPad and Deploy 🚀

### 7.1 Connect Your iPad

1. **Connect iPad** to Mac via USB cable
2. **Unlock iPad**
3. If prompted "Trust This Computer?", tap **Trust**
4. Enter your iPad passcode if requested

### 7.2 Select Your iPad in Xcode

1. In Xcode, find the device selector (top left, near Play button)
2. Click it and select your iPad from the list
3. If you don't see it:
   - Make sure iPad is unlocked
   - Try disconnecting and reconnecting
   - Go to **Window > Devices and Simulators** to see if it's detected

### 7.3 Build and Run!

1. Click the **▶️ Play button** (or press Cmd + R)
2. Xcode will:
   - Compile the code
   - Copy files to iPad
   - Install the app
   - Launch it

**First time**: This build takes 5-10 minutes.

### 7.4 Trust Developer Certificate (First Time Only)

If you see "Untrusted Developer" on iPad:

1. On your **iPad**, go to: **Settings**
2. Go to: **General** → **VPN & Device Management**
3. Find your **Apple ID** under "Developer App"
4. Tap it
5. Tap **Trust "[Your Apple ID]"**
6. Confirm by tapping **Trust**
7. Return to home screen and launch the app again

---

## Step 8: Test the App! 🌅

The app should now be running on your iPad!

### Quick Test Checklist:

- [ ] App launches without crashing
- [ ] You see the main screen with current time
- [ ] Tap **"Test Sunrise"** - watch the 30-second demo
- [ ] Tap **"Add Alarm"** - create a test alarm
- [ ] Tap **"Settings"** - adjust sunrise duration
- [ ] Close app and reopen - settings should persist

### For Best Results:

1. **Set iPad to max brightness**:
   - Settings → Display & Brightness → Move slider to max
   - Turn OFF "Auto-Brightness"

2. **Enable guided access** (optional, keeps app in foreground):
   - Settings → Accessibility → Guided Access
   - Turn it ON
   - Set a passcode

3. **Disable auto-lock**:
   - Settings → Display & Brightness → Auto-Lock → Never
   - (Or keep iPad plugged in)

---

## 🎯 Quick Reference Commands

Save these for future rebuilds:

```bash
# Navigate to kivy-ios
cd ~/kivy-projects/kivy-ios

# Rebuild app (after code changes)
python3 toolchain.py create SunriseAlarm /path/to/sunrise-alarm-app --force

# Open in Xcode
open SunriseAlarm-ios/SunriseAlarm.xcodeproj

# Then in Xcode: Just click ▶️ to rebuild and deploy
```

---

## ❓ Troubleshooting

### "Build Failed" in Xcode

**Check**:
- Make sure you selected your iPad (not a simulator)
- Check Bundle Identifier is unique
- Verify Team is selected in Signing

**Try**:
1. Product → Clean Build Folder (Cmd + Shift + K)
2. Rebuild (Cmd + R)

### "Could not launch" or App Crashes

**View crash logs**:
1. Xcode → Window → Devices and Simulators
2. Select your iPad
3. Click "View Device Logs"
4. Look for SunriseAlarm crashes

**Common fix**:
```bash
# Rebuild the Xcode project
cd ~/kivy-projects/kivy-ios
python3 toolchain.py create SunriseAlarm /path/to/app --force
```

### iPad Not Showing in Xcode

**Try**:
1. Disconnect and reconnect USB
2. Restart Xcode
3. Unlock iPad
4. Window → Devices and Simulators (check if iPad appears)

### "kivy-ios build failed"

**Clean and rebuild**:
```bash
cd ~/kivy-projects/kivy-ios
python3 toolchain.py clean python3
python3 toolchain.py clean kivy
python3 toolchain.py build python3
python3 toolchain.py build kivy
```

---

## 🔄 Updating the App After Changes

If you modify the code and want to redeploy:

**Option 1: Quick (if only Python code changed)**
1. Open Xcode project
2. Click ▶️ to rebuild
3. Xcode will copy updated main.py

**Option 2: Full rebuild (if structure changed)**
```bash
cd ~/kivy-projects/kivy-ios
python3 toolchain.py create SunriseAlarm /path/to/app --force
open SunriseAlarm-ios/SunriseAlarm.xcodeproj
# Click ▶️ in Xcode
```

---

## 📞 Need Help?

1. **Check DEPLOYMENT.md** for detailed troubleshooting
2. **Check TROUBLESHOOTING.md** for installation issues
3. **Kivy-iOS issues**: https://github.com/kivy/kivy-ios/issues
4. **Kivy community**: https://chat.kivy.org/

---

## ✅ Success!

Once deployed, you can:
- 🌅 Wake up naturally with sunrise simulation
- ⏰ Set weekly routines
- 📱 Use your iPad as a dedicated alarm clock

**Enjoy your natural wake-up experience!** 🌟
