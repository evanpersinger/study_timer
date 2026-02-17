# Study Timer

A simple, effective Pomodoro-style study timer built with Python and tkinter. Perfect for students who need focused study sessions with comprehensive progress tracking and integrated Spotify background music!

## Features

- **Two Preset Modes:**
  - 25 minute study / 5 minute break (Classic Pomodoro)
  - 50 minute study / 10 minute break (Extended Pomodoro)
- **Test Mode** - 5-second test mode for quick testing of timer functions (can be enabled in code)
- **Dual Timer Display** - Shows both current countdown and next session duration
- **Smart Audio Notifications** - Different sounds for different study durations (Glass for 25min, Ping for 50min) with adjustable playback speed
- **Binaural Beat Audio** - Plays a local 40Hz binaural beat audio file during study sessions for enhanced focus and concentration
- **Manual Control** - Start Break and Start Study buttons for flexible timing
- **Smart Session Tracking** - Counts partial sessions as decimals (e.g., 0.5 for half a session) plus tracks total study time
- **Daily Data Collection** - Tracks sessions and study time with automatic daily reset
- **Historical Data Storage** - Saves all daily data in one organized file for long-term tracking
- **Real-time Progress Display** - Live session count and total study time at bottom of interface
- **Cross-Platform Audio** - Works on Windows (winsound), macOS (afplay), and Linux (paplay)
- **Modern Dark Theme Interface** - Clean, distraction-free GUI with:
  - White-bordered labels for "Study Timer", "Study", and "Break"
  - Hover effects (grey background) on interactive elements
  - Custom button hover effects
  - Frameless window design (no title bar)
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
   - (Optional) Enable "TEST (5 sec)" button in code for quick testing

3. **Start studying:**
   - Click "Start" to begin your study session
   - The binaural beat audio will automatically play (if the binaural_beat.mp3 file exists)
   - The left timer shows your current countdown, right timer shows next session duration
   - When study time ends, click "Start Break" when you're ready for a break
   - Audio will pause during your break
   - When break time ends, click "Start Study" to resume (audio will start again)
   - Click "Pause" to pause the timer and audio
   - Click "Stop" to stop the notification sound
   - Click "Reset" to start over

4. **Track your progress:**
   - View session count (including partial sessions as decimals) and total study time displayed at the bottom
   - Partial sessions count as decimals (e.g., 0.5 for half a session, 0.8 for 80% completion)
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
    "session_count": 3.5,
    "total_study_time": 87.5,
    "last_updated": "2025-01-15T14:30:00.000000"
  }
}
```

**Data Fields:**
- `session_count`: Total sessions completed (including partial sessions as decimals)
- `total_study_time`: Total minutes studied (can include partial minutes)
- `last_updated`: Timestamp of last data update

## Installation

Minimal dependencies required for basic usage!

### Quick Start

```bash
# Clone or download this project
cd study_timer

# Setup data file (first time only)
cp data/data_example.json data/data.json

# Install dependencies (includes Spotify integration)
uv pip install -r requirements.txt

# Run the timer
python study_timer.py
```

### Audio Setup

To enable binaural beat audio during study sessions:

1. **Ensure audio file exists:**
   - Place a `binaural_beat.mp3` file in the project root directory
   - The app will automatically play this file during study sessions

The app will automatically play the 40Hz binaural beat when you start a study session and pause it during breaks.

### Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
uv pip install -r requirements.txt

# Run the timer
python study_timer.py
```

## System Requirements

- Python 3.6 or higher
- tkinter (usually comes with Python)
- Audio system for notifications and binaural beat playback

## Tips for Effective Study Sessions

1. **Choose the right preset** - Use 25/5 for intense focus, 50/10 for longer reading sessions
2. **Use manual control** - Click "Start Break" and "Start Study" when you're ready, not when the timer says
3. **Eliminate distractions** - Close unnecessary apps and notifications
4. **Take breaks seriously** - Step away from your desk during break time
5. **Track your progress** - Monitor your daily sessions (including partial sessions as decimals) and total study time in real-time at the bottom
6. **Build habits** - Use the session counter to maintain consistent study routines
7. **Stop notifications** - Click "Stop" to silence the notification sound when you're ready
8. **Don't worry about interruptions** - Partial sessions count as decimals (e.g., 0.5 for half a session) so you get credit for partial work
9. **Use the dual display** - The right timer shows your next session duration for better planning
10. **Data persistence** - Your progress is automatically saved, so you can close and reopen anytime

## Troubleshooting

- **No sound notifications?** The timer will still work, just check the popup messages. On macOS, sounds use system audio files.
- **Binaural beat not playing?** Make sure the `binaural_beat.mp3` file exists in the project root directory.
- **GUI not appearing?** Make sure you have tkinter installed: `python -m tkinter`
- **Timer not accurate?** The timer updates every second, slight delays are normal
- **Data not saving?** Make sure the `data/` directory exists and you have write permissions
- **Virtual environment issues?** Make sure you've activated your virtual environment before running
- **Audio not working on Linux?** Install paplay/pulseaudio: `sudo apt-get install pulseaudio-utils`

Happy studying!
