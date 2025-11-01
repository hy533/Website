# Quick Start Guide

Get your Sunrise Alarm Clock running in 5 minutes!

## Test on Your Computer First (Recommended)

Before deploying to iPad, test the app on your computer to see how it works.

### macOS / Linux

```bash
cd sunrise-alarm-app
./run.sh
```

### Windows

```bash
cd sunrise-alarm-app
run.bat
```

### Manual Method (All Platforms)

```bash
cd sunrise-alarm-app
pip install -r requirements.txt
python main.py
```

## Quick Tutorial

Once the app is running:

### 1. Test the Sunrise Effect

- Click **"Test Sunrise"** button on main screen
- Watch a quick 30-second sunrise animation
- See the screen transition from dark purple → orange → bright yellow
- Click **"Stop Alarm"** to return to main screen

### 2. Add Your First Alarm

- Click **"Add Alarm"**
- Set time (24-hour format):
  - Hour: 07 (7 AM)
  - Minute: 00
- Select days:
  - Click **"Weekdays"** for Monday-Friday
  - Or tap individual day buttons
- Click **"Save Alarm"**

### 3. Configure Settings

- Click **"Settings"** on main screen
- Adjust **"Sunrise Duration"** slider:
  - 20 minutes = faster wake-up
  - 30 minutes = default
  - 45 minutes = very gentle wake-up
- Enable **"Keep Screen On"** (recommended)
- Click **"Back"**

### 4. Manage Alarms

On the main screen:
- **Toggle ON/OFF**: Enable or disable alarm without deleting
- **Delete**: Remove alarm completely
- **View Time**: See all your scheduled alarms

## Understanding the Sunrise

The app simulates a natural sunrise in 4 phases:

1. **Night (0-20%)**: Deep purple/blue - Very dim
2. **Dawn (20-40%)**: Purple to orange - Gradually brightening
3. **Sunrise (40-70%)**: Orange to red/yellow - Getting brighter
4. **Morning (70-100%)**: Bright yellow - Full brightness

The entire process takes your configured duration (default: 30 minutes).

## iPad Deployment - Next Steps

Once you've tested the app and are happy with it, deploy to your iPad:

### Easiest Method: Just Run It!

If you have a Mac and Xcode:

```bash
# Install dependencies (one-time setup)
brew install autoconf automake libtool pkg-config
pip3 install Cython==0.29.36

# Clone kivy-ios
git clone https://github.com/kivy/kivy-ios.git
cd kivy-ios

# Build for iOS (takes 30-60 minutes, one-time)
python3 toolchain.py build python3
python3 toolchain.py build kivy

# Create Xcode project
python3 toolchain.py create SunriseAlarm /path/to/sunrise-alarm-app

# Open in Xcode
open SunriseAlarm-ios/SunriseAlarm.xcodeproj

# In Xcode:
# 1. Connect iPad
# 2. Select your device
# 3. Click Run ▶️
```

For detailed instructions, see **DEPLOYMENT.md**

## Tips for Best Experience

### On Computer

- Maximize the window for full effect
- Test different sunrise durations
- Try setting an alarm for 1 minute from now to see how it triggers

### On iPad

- Set iPad to maximum brightness
- Disable auto-brightness
- Enable "Do Not Disturb" mode
- Keep iPad plugged in while alarm is active
- Position iPad facing you on bedside table

## Troubleshooting

### "No module named 'kivy'"

```bash
pip install kivy
# or
pip3 install kivy
```

### Window is too small

The app will size based on your screen. On computer:
- Maximize the window
- Or edit window size in code (see README.md)

### Colors look wrong

- Ensure your display brightness is up
- Check if Night Shift/blue light filter is on (disable for testing)
- Try running the Test Sunrise multiple times

### Alarm doesn't trigger

- Ensure alarm is toggled ON
- Check the correct day is selected
- Time is in 24-hour format (14:30 = 2:30 PM)
- App must be running for alarms to trigger

## What's Next?

1. **Test thoroughly** on your computer
2. **Customize** sunrise duration in settings
3. **Set up weekly routines** that match your schedule
4. **Deploy to iPad** following DEPLOYMENT.md
5. **Enjoy natural wake-ups!** 🌅

## Need More Help?

- **Full documentation**: See README.md
- **iPad deployment**: See DEPLOYMENT.md
- **Technical details**: See code comments in main.py

---

**Happy waking! 🌅**
