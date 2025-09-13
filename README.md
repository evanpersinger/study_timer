# Study Timer

A simple, effective Pomodoro-style study timer built with Python and tkinter. Perfect for students who need focused study sessions with comprehensive progress tracking!

## Features

- **Two Preset Modes:**
  - 25 minute study / 5 minute break (Classic Pomodoro)
  - 50 minute study / 10 minute break (Extended Pomodoro)
- **Dual Timer Display** - Shows both current countdown and next session duration
- **Smart Audio Notifications** - Different sounds for different study durations (Glass for 25min, Ping for 50min)
- **Manual Control** - Start Break and Start Study buttons for flexible timing
- **Partial Session Tracking** - Automatically tracks partial study time when sessions are interrupted
- **Daily Data Collection** - Tracks sessions and study time with automatic daily reset
- **Historical Data Storage** - Saves all daily data in one organized file for long-term tracking
- **Real-time Progress Display** - Live session count and total study time at bottom of interface
- **Cross-Platform Audio** - Works on Windows (winsound), macOS (afplay), and Linux (paplay)
- **Dark Theme Interface** - Clean, distraction-free GUI with custom button hover effects
- **Automatic Data Persistence** - Saves progress automatically and loads on startup

## How to Use

1. **Setup (first time only):**
   ```bash
   # Copy the data template
   cp data/data_example.json data/data.json
   
   # Run the timer
   python study_timer.py
   ```

2. **Choose your preset:**
   - Click "25 min study / 5 min break" for classic Pomodoro
   - Click "50 min study / 10 min break" for longer sessions

3. **Start studying:**
   - Click "Start" to begin your study session
   - The left timer shows your current countdown, right timer shows next session duration
   - When study time ends, click "Start Break" when you're ready for a break
   - When break time ends, click "Start Study" when you're ready to continue
   - Click "Pause" to pause the timer
   - Click "Stop" to stop the notification sound
   - Click "Reset" to start over

4. **Track your progress:**
   - View completed sessions and total study time displayed at the bottom
   - Partial study time is automatically tracked if you pause or reset mid-session
   - Daily data automatically resets each day but preserves historical data

## Data Collection

The Study Timer automatically collects and stores your daily study data:

- **Single Data File**: All daily data is saved to `data/data.json`
- **Automatic Reset**: Session count and study time reset to 0 each new day
- **Historical Data**: Previous days' data is preserved in the same file
- **Privacy**: All data is stored locally on your computer
- **Real-time Tracking**: See your progress displayed live during study sessions

### Getting Started

1. **Copy the template file:**
   ```bash
   cp data/data_example.json data/data.json
   ```

2. **Run the timer:**
   ```bash
   python study_timer.py
   ```

The app will automatically create and use your personal `data.json` file for tracking your study sessions.

### Data Structure
The data file contains all days organized by date:
```json
{
  "2025-01-15": {
    "session_count": 3,
    "total_study_time": 75,
    "last_updated": "2025-01-15T14:30:00.000000"
  }
}
```

## Installation

No external dependencies required! This uses only Python standard library modules.

### Quick Start

```bash
# Clone or download this project
cd study_timer

# Setup data file (first time only)
cp data/data_example.json data/data.json

# Run the timer
python study_timer.py
```

### Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Run the timer
python study_timer.py
```

## System Requirements

- Python 3.6 or higher
- tkinter (usually comes with Python)
- Audio system for notifications

## Tips for Effective Study Sessions

1. **Choose the right preset** - Use 25/5 for intense focus, 50/10 for longer reading sessions
2. **Use manual control** - Click "Start Break" and "Start Study" when you're ready, not when the timer says
3. **Eliminate distractions** - Close unnecessary apps and notifications
4. **Take breaks seriously** - Step away from your desk during break time
5. **Track your progress** - Monitor your daily sessions and total study time in real-time at the bottom
6. **Build habits** - Use the session counter to maintain consistent study routines
7. **Stop notifications** - Click "Stop" to silence the notification sound when you're ready
8. **Don't worry about interruptions** - Partial study time is automatically tracked if you pause or reset
9. **Use the dual display** - The right timer shows your next session duration for better planning
10. **Data persistence** - Your progress is automatically saved, so you can close and reopen anytime

## Troubleshooting

- **No sound notifications?** The timer will still work, just check the popup messages. On macOS, sounds use system audio files.
- **GUI not appearing?** Make sure you have tkinter installed: `python -m tkinter`
- **Timer not accurate?** The timer updates every second, slight delays are normal
- **Data not saving?** Make sure the `data/` directory exists and you have write permissions
- **Virtual environment issues?** Make sure you've activated your virtual environment before running
- **Audio not working on Linux?** Install pulseaudio: `sudo apt-get install pulseaudio-utils`

Happy studying! 📚⏰
