# Study Timer

A simple, effective Pomodoro-style study timer built with Python and tkinter. Perfect for data science students who need focused study sessions!

## Features

- **Two Preset Modes:**
  - 25 minute study / 5 minute break (Classic Pomodoro)
  - 50 minute study / 10 minute break (Extended Pomodoro)
- **Visual Timer Display** - Large, easy-to-read countdown with Study/Break labels
- **Audio Notifications** - Beeps when study/break sessions complete
- **Manual Control** - Start Break and Start Study buttons for flexible timing
- **Daily Data Collection** - Tracks sessions and study time with automatic daily reset
- **Historical Data Storage** - Saves daily data files for long-term tracking
- **Session Tracking** - Real-time display of completed sessions and total study time
- **Cross-Platform** - Works on Windows, macOS, and Linux
- **Simple GUI** - Clean, distraction-free interface with custom button hover effects

## How to Use

1. **Run the timer:**
   ```bash
   python study_timer.py
   ```

2. **Choose your preset:**
   - Click "25 min Study / 5 min Break" for classic Pomodoro
   - Click "50 min Study / 10 min Break" for longer sessions

3. **Start studying:**
   - Click "Start" to begin your study session
   - When study time ends, click "Start Break" when you're ready for a break
   - When break time ends, click "Start Study" when you're ready to continue
   - Click "Pause" to pause the timer
   - Click "Stop" to stop the notification sound
   - Click "Reset" to start over

4. **Track your progress:**
   - View completed sessions and total study time at the bottom
   - Click "View Data" to see today's study statistics
   - Daily data automatically resets each day but preserves historical data

## Data Collection

The Study Timer automatically collects and stores your daily study data:

- **Daily Files**: Each day's data is saved to `study_data/study_data_YYYY-MM-DD.json`
- **Automatic Reset**: Session count and study time reset to 0 each new day
- **Historical Data**: Previous days' data is preserved in separate files
- **Privacy**: All data is stored locally on your computer
- **View Data**: Click "View Data" button to see today's statistics

### Data Structure
Each daily file contains:
```json
{
  "date": "2024-01-15",
  "session_count": 3,
  "total_study_time": 75,
  "last_updated": "2024-01-15T14:30:00"
}
```

## Installation

No external dependencies required! This uses only Python standard library modules.

```bash
# Clone or download this project
cd study_timer

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
5. **Track your progress** - Use the "View Data" button to see your daily study statistics
6. **Build habits** - Check your daily data to maintain consistent study routines
7. **Stop notifications** - Click "Stop" to silence the notification sound when you're ready

## Troubleshooting

- **No sound notifications?** The timer will still work, just check the popup messages
- **GUI not appearing?** Make sure you have tkinter installed: `python -m tkinter`
- **Timer not accurate?** The timer updates every second, slight delays are normal

Happy studying! 📚⏰
