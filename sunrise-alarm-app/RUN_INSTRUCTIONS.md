# HOW TO TEST RUN THE APP

The code is installed and verified! Here's how to run it on YOUR computer:

## Option 1: Automatic (Easiest) 🚀

### On Mac or Linux:
```bash
cd /path/to/sunrise-alarm-app
./run.sh
```

### On Windows:
```bash
cd \path\to\sunrise-alarm-app
run.bat
```

The script will automatically:
- Check if Python is installed
- Install Kivy if needed
- Launch the app

## Option 2: Manual 📝

```bash
# Navigate to the app folder
cd /path/to/sunrise-alarm-app

# Install dependencies (first time only)
pip install kivy
# or on some systems:
pip3 install kivy

# Run the app
python main.py
# or on some systems:
python3 main.py
```

## What You'll See 👀

When the app launches, you'll see:

1. **Main Screen**:
   - Large clock showing current time
   - List of your alarms (empty at first)
   - "Add Alarm" button (green)
   - "Test Sunrise" button (orange) ← **Try this first!**
   - "Settings" button (blue)

2. **Click "Test Sunrise" to see a demo**:
   - Screen goes black
   - Gradually turns purple, then orange, then bright yellow
   - Takes 30 seconds (instead of full 30 minutes)
   - Shows current time
   - "Stop Alarm" button to end it

3. **Try adding an alarm**:
   - Click "Add Alarm"
   - Select time (hour and minute)
   - Choose days (or use presets)
   - Click "Save Alarm"

## Controls 🎮

- **Mouse**: Click buttons and interact
- **ESC**: Quit the app
- **Cmd+Q** (Mac) or **Alt+F4** (Windows): Also quits

## What to Test ✓

1. ✓ **Test Sunrise button** - See the color animation
2. ✓ **Add an alarm** - Set for 1-2 minutes from now
3. ✓ **Wait for alarm** - Keep app open and watch it trigger
4. ✓ **Try Settings** - Adjust sunrise duration
5. ✓ **Toggle alarm on/off** - Use the ON/OFF button
6. ✓ **Delete alarm** - Use the Delete button
7. ✓ **Quick presets** - Try "Weekdays", "Weekend", "Every Day"

## Common Issues 🔧

### "python: command not found"
Try `python3` instead of `python`

### "No module named 'kivy'"
Run: `pip install kivy` or `pip3 install kivy`

### Window is small
Maximize the window, or it will size based on your screen

### App won't start
Make sure you're in the right directory:
```bash
ls main.py
# Should show: main.py
```

## Where is the app?

The app is located at:
```
/home/user/Website/sunrise-alarm-app/
```

On YOUR computer, it's wherever you cloned/downloaded the repository.

## Next Steps After Testing

Once you've tested and are happy with it:

1. **Read DEPLOYMENT.md** - Detailed iPad deployment guide
2. **Customize** - Edit colors/timing in main.py if desired
3. **Deploy to iPad** - Follow the iOS build instructions

---

**Ready to test? Run the command for your system above!** 🌅
