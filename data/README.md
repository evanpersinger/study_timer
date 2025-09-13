# Study Timer Data Directory

This directory contains study session data collected by the Study Timer application.

## File Format

All daily data is stored in a single JSON file:
`data.json`

## Data Structure

The file contains all days organized by date:
```json
{
  "2024-01-14": {
    "session_count": 4,
    "total_study_time": 100,
    "last_updated": "2024-01-14T23:45:30.123456"
  },
  "2024-01-15": {
    "session_count": 3,
    "total_study_time": 75,
    "last_updated": "2024-01-15T14:30:00"
  }
}
```

## How It Works

- **Daily Reset**: Each day starts fresh with 0 sessions and 0 minutes
- **Historical Data**: Previous days' data is preserved in the same file
- **Automatic Updates**: Data is updated automatically when you complete study sessions
- **Data Persistence**: All data is saved automatically and persists between app sessions

## Viewing Your Data

- Use the "View Data" button in the Study Timer app to see today's statistics
- The data.json file can be opened directly to view all historical data
- Each date entry represents one day of study activity

## Privacy

All data is stored locally on your computer. No data is sent to external servers.
