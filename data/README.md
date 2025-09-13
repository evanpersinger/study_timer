# Study Timer Data Directory

This directory contains study session data collected by the Study Timer application.

## File Format

All daily data is stored in a single JSON file:
`data.json`

## Getting Started

1. **Copy the template file:**
   ```bash
   cp data/data_example.json data/data.json
   ```

2. **Run the Study Timer:**
   ```bash
   python study_timer.py
   ```

The app will automatically use your personal `data.json` file for tracking your study sessions.

## Files in this Directory

- `data_example.json` - Template file showing the expected data structure
- `data.json` - Your personal study data (created when you copy the template)

## Data Structure

The file contains all days organized by date:
```json
{
  "2025-01-15": {
    "session_count": 3,
    "total_study_time": 75,
    "last_updated": "2025-01-15T14:30:00.000000"
  }
}
```

## How It Works

- **Daily Reset**: Each day starts fresh with 0 sessions and 0 minutes
- **Historical Data**: Previous days' data is preserved in the same file
- **Automatic Updates**: Data is updated automatically when you complete study sessions
- **Data Persistence**: All data is saved automatically and persists between app sessions

## Viewing Your Data

- View your progress in real-time on the Study Timer app's main interface
- The data.json file can be opened directly to view all historical data
- Each date entry represents one day of study activity

## Privacy

All data is stored locally on your computer. No data is sent to external servers.
