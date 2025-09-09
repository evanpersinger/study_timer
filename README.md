# Study Timer

A simple, effective Pomodoro-style study timer built with Python and tkinter. Perfect for data science students who need focused study sessions!

## Features

- **Two Preset Modes:**
  - 25 minute study / 5 minute break (Classic Pomodoro)
  - 50 minute study / 10 minute break (Extended Pomodoro)
- **Visual Timer Display** - Large, easy-to-read countdown
- **Audio Notifications** - Beeps when study/break sessions complete
- **Session Tracking** - Counts completed sessions and total study time
- **Cross-Platform** - Works on Windows, macOS, and Linux
- **Simple GUI** - Clean, distraction-free interface

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
   - The timer will automatically switch between study and break periods
   - Click "Pause" to pause the timer
   - Click "Reset" to start over

4. **Track your progress:**
   - View completed sessions and total study time at the bottom

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
2. **Eliminate distractions** - Close unnecessary apps and notifications
3. **Take breaks seriously** - Step away from your desk during break time
4. **Track your progress** - Use the session counter to build study habits
5. **Stay consistent** - Try to complete full cycles (study + break)

## Troubleshooting

- **No sound notifications?** The timer will still work, just check the popup messages
- **GUI not appearing?** Make sure you have tkinter installed: `python -m tkinter`
- **Timer not accurate?** The timer updates every second, slight delays are normal

Happy studying! 📚⏰
