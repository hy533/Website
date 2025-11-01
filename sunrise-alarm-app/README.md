# Sunrise Alarm Clock for iPad

A beautiful Python-based alarm clock app that simulates a natural sunrise to wake you up gently. Built with Kivy framework for cross-platform compatibility.

## Features

- 🌅 **Realistic Sunrise Simulation**: Gradually transitions from deep purple/blue (night) through orange/red (dawn) to bright yellow (morning)
- ⏰ **Multiple Alarms**: Set as many alarms as you need
- 📅 **Weekly Routines**: Configure different wake-up times for different days of the week
- 🎨 **Beautiful UI**: Designed specifically for iPad with touch-friendly controls
- ⚙️ **Customizable**: Adjust sunrise duration (10-60 minutes)
- 💾 **Persistent Storage**: All alarms and settings are saved automatically

## Screenshots

The app includes:
- **Main Screen**: View all your alarms, current time, and quick access to settings
- **Add Alarm Screen**: Set time and select days with convenient presets (Weekdays, Weekend, Every Day)
- **Sunrise Screen**: Full-screen sunrise animation with time display and stop button
- **Settings Screen**: Customize sunrise duration and other preferences

## Quick Start - Test on Your Computer First

Before deploying to iPad, test the app on your computer:

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Navigate to the app directory:**
   ```bash
   cd sunrise-alarm-app
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app:**
   ```bash
   python main.py
   ```

The app will open in a window. You can:
- Click "Add Alarm" to create alarms
- Use "Test Sunrise" to see a quick 30-second sunrise animation
- Configure settings like sunrise duration

## Deploying to iPad

There are **two main methods** to get this app on your iPad:

### Method 1: Using Kivy Launcher (Easiest - No Development Account Required)

1. **Install Kivy Launcher on your iPad:**
   - Download from App Store: [Kivy Launcher](https://apps.apple.com/app/kivy-launcher/id1234567890)
   - Note: Kivy Launcher may have limited availability

2. **Transfer the app:**
   - Copy the entire `sunrise-alarm-app` folder to your iPad using iTunes File Sharing or a cloud service
   - Place it in the Kivy Launcher's documents folder

3. **Launch:**
   - Open Kivy Launcher
   - Select "Sunrise Alarm"

### Method 2: Build Native iOS App (Requires macOS)

This method creates a standalone iOS app you can install via Xcode.

#### Prerequisites
- Mac computer with macOS
- Xcode installed (from Mac App Store)
- Apple Developer Account (free account works for personal use)
- Homebrew package manager

#### Step-by-Step Guide

1. **Install Kivy-iOS toolchain on your Mac:**

   ```bash
   # Install dependencies
   brew install autoconf automake libtool pkg-config
   brew install sdl2 sdl2_image sdl2_mixer sdl2_ttf

   # Install Cython
   pip3 install Cython==0.29.36

   # Clone and setup kivy-ios
   git clone https://github.com/kivy/kivy-ios.git
   cd kivy-ios
   ```

2. **Build the required libraries:**

   ```bash
   # Build Python for iOS
   ./toolchain.py build python3

   # Build Kivy
   ./toolchain.py build kivy
   ```

   This process can take 30-60 minutes depending on your Mac's speed.

3. **Create your Xcode project:**

   ```bash
   # From the kivy-ios directory
   ./toolchain.py create SunriseAlarm /path/to/sunrise-alarm-app
   ```

   Replace `/path/to/sunrise-alarm-app` with the actual path to your app folder.

4. **Open in Xcode:**

   ```bash
   open SunriseAlarm-ios/SunriseAlarm.xcodeproj
   ```

5. **Configure signing:**
   - In Xcode, select the project in the left sidebar
   - Go to "Signing & Capabilities"
   - Select your Apple Developer team
   - Change the bundle identifier if needed (must be unique)

6. **Deploy to iPad:**
   - Connect your iPad via USB
   - Select your iPad from the device menu in Xcode
   - Click the "Play" button to build and run
   - First time: Go to Settings > General > Device Management on iPad and trust your developer certificate

### Method 3: Alternative - Using Pythonista (iPad App)

1. **Install Pythonista from App Store:**
   - Purchase and install [Pythonista](https://apps.apple.com/app/pythonista-3/id1085978097)
   - It's a paid app but very useful for running Python on iOS

2. **Transfer the code:**
   - Copy `main.py` to Pythonista
   - Note: You may need to adapt some features as Pythonista has its own iOS integration

3. **Install Kivy in Pythonista:**
   - This requires additional steps and may not support all Kivy features
   - Refer to Pythonista documentation for package installation

## Usage Guide

### Setting Up Your First Alarm

1. **Open the app** and tap "Add Alarm"

2. **Choose your wake-up time:**
   - Use the hour and minute spinners to select your desired time
   - Time is in 24-hour format (00:00 to 23:59)

3. **Select days:**
   - Tap individual day buttons to toggle them on/off
   - Or use quick presets:
     - **Weekdays**: Monday-Friday
     - **Weekend**: Saturday-Sunday
     - **Every Day**: All days

4. **Save**: Tap "Save Alarm"

### Managing Alarms

- **Enable/Disable**: Tap the ON/OFF toggle next to each alarm
- **Delete**: Tap the "Delete" button
- **Test**: Use "Test Sunrise" on main screen for a quick 30-second preview

### Settings

- **Sunrise Duration**: Adjust how long the sunrise animation lasts (10-60 minutes)
  - Shorter duration: Brighter, faster wake-up
  - Longer duration: Gentler, more gradual wake-up
  - Default: 30 minutes

- **Keep Screen On**: When enabled, prevents iPad from sleeping during alarm

### The Sunrise Experience

When an alarm triggers:

1. **Screen gradually brightens** following a natural sunrise pattern:
   - Deep purple/blue (night) → 0-20%
   - Purple/orange (dawn) → 20-40%
   - Orange/red (sunrise) → 40-70%
   - Yellow/bright (morning) → 70-100%

2. **Time is displayed** in large, easy-to-read format

3. **Stop button appears** to dismiss the alarm when you're awake

## Tips for Best Results

1. **iPad Placement:**
   - Place iPad on a bedside table facing you
   - Angle it so the light reaches your face
   - Ensure it's plugged in (don't rely on battery)

2. **Brightness Settings:**
   - Set iPad brightness to maximum before sleep
   - Disable auto-brightness in iPad settings
   - Enable "Do Not Disturb" to prevent other notifications

3. **Recommended Settings:**
   - First-time users: Start with 30-minute sunrise duration
   - Light sleepers: Try 20-25 minutes
   - Heavy sleepers: Use 30-45 minutes

4. **For Best Sleep:**
   - Use Night Shift or reduce blue light before bed
   - Keep a consistent wake-up schedule

## Troubleshooting

### App doesn't open
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check Python version: `python --version` (should be 3.8+)
- Try reinstalling Kivy: `pip install --upgrade kivy`

### Alarms not triggering
- Check that alarm is enabled (toggle shows "ON")
- Verify correct day is selected
- Ensure iPad is not in sleep mode (enable "Keep Screen On" in settings)
- Check that date/time on iPad is correct

### Sunrise looks wrong
- Verify iPad brightness is at maximum
- Check that auto-brightness is disabled
- Ensure iPad is in full-screen mode

### iPad goes to sleep
- Enable "Keep Screen On" in app settings
- In iPad Settings > Display & Brightness, set Auto-Lock to "Never"
- Ensure iPad is charging

## Technical Details

- **Framework**: Kivy 2.2.1+
- **Language**: Python 3.8+
- **Platform**: iOS/iPadOS 12.0+
- **Storage**: Uses local JSON files for alarms and settings
- **Display**: Optimized for iPad screen sizes (9.7" - 12.9")

## File Structure

```
sunrise-alarm-app/
├── main.py              # Main application code
├── requirements.txt     # Python dependencies
├── buildozer.spec      # Build configuration for iOS
├── README.md           # This file
└── DEPLOYMENT.md       # Detailed deployment guide
```

## Customization

The code is well-commented and organized. You can customize:

- **Colors**: Modify the sunrise color phases in `SunriseScreen.update_sunrise()`
- **UI Layout**: Adjust layouts in each Screen class
- **Animation Speed**: Change the Clock schedule intervals
- **Sounds**: Add audio support (requires additional dependencies)

## Future Enhancements

Potential features to add:
- Custom alarm sounds or music
- Fade-in audio alarm
- Snooze functionality
- Multiple alarm profiles
- Gradual volume increase
- Weather integration
- Sleep tracking

## Credits

Built with:
- [Kivy](https://kivy.org/) - Open source Python framework for multi-touch applications
- [Kivy-iOS](https://github.com/kivy/kivy-ios) - Toolchain to compile Kivy applications for iOS

## License

This project is open source. Feel free to modify and customize for your personal use.

## Support

For issues or questions:
1. Check the Troubleshooting section above
2. Review Kivy documentation: https://kivy.org/doc/stable/
3. Kivy-iOS documentation: https://github.com/kivy/kivy-ios

---

**Enjoy your natural wake-up experience! 🌅**
