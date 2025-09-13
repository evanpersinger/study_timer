# Study Timer Data Directory

This directory contains daily study session data collected by the Study Timer application.

## File Format

Each day's data is stored in a separate JSON file with the format:
`study_data_YYYY-MM-DD.json`

Example: `study_data_2024-01-15.json`

## Data Structure

Each file contains:
```json
{
  "date": "2024-01-15",
  "session_count": 3,
  "total_study_time": 75,
  "last_updated": "2024-01-15T14:30:00"
}
```

## How It Works

- **Daily Reset**: Each day starts fresh with 0 sessions and 0 minutes
- **Historical Data**: Previous days' data is preserved in separate files
- **Automatic Creation**: Files are created automatically when you complete study sessions
- **Data Persistence**: All data is saved automatically and persists between app sessions

## Viewing Your Data

- Use the "View Data" button in the Study Timer app to see today's statistics
- Historical data files can be opened directly to view past days' data
- Each file represents one day of study activity

## Privacy

All data is stored locally on your computer. No data is sent to external servers.
