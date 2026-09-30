# google-data-utils

Simple utilities for loading public Google Drive CSV files, Excel files, and Google Sheets into pandas DataFrames.

> **Note**
>
> This package only supports publicly accessible Google Drive files and Google Sheets. Authentication, OAuth, and Google API credentials are not required.

## Features

- Read public Google Drive CSV files into a DataFrame
- Read public Google Drive Excel files into a DataFrame
- Read public Google Sheets into a DataFrame
- Validate Google Drive and Google Sheets URLs
- Extract Google Drive file IDs and Google Sheets IDs
- No API keys required
- No OAuth required
- No Google Cloud setup required

## Installation

```bash
pip install google-data-utils
```

## Usage

### Google Drive CSV

```bash
from google_data_utils import google_csv_to_df

df = google_csv_to_df(
    "https://drive.google.com/file/d/FILE_ID/view?usp=sharing"
)
```

### Google Drive Excel

```bash
from google_data_utils import google_excel_to_df

df = google_excel_to_df(
    "https://drive.google.com/file/d/FILE_ID/view?usp=sharing"
)
```

### Google Sheets

```bash
from google_data_utils import google_sheet_to_df

df = google_sheet_to_df(
    "https://docs.google.com/spreadsheets/d/SHEET_ID/edit#gid=0"
)
```

### URL Validation

```bash
from google_data_utils import (
    is_google_drive_url,
    is_google_sheet_url,
)

is_google_drive_url(
    "https://drive.google.com/file/d/FILE_ID/view"
)
# True

is_google_sheet_url(
    "https://docs.google.com/spreadsheets/d/SHEET_ID/edit"
)
# True
```

### Extract IDs

```bash
from google_data_utils import (
    extract_drive_file_id,
    extract_sheet_id,
)

extract_drive_file_id(
    "https://drive.google.com/file/d/FILE_ID/view"
)
# FILE_ID

extract_sheet_id(
    "https://docs.google.com/spreadsheets/d/SHEET_ID/edit"
)
# SHEET_ID
```

### Requirements

```text
Python 3.8+
pandas
openpyxl
```

### License

```text
MIT License
```
