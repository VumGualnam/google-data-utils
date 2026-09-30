# public.py

import pandas as pd

from .validators import (
    extract_drive_file_id,
    extract_sheet_id,
)


    
def google_csv_to_df(url, **kwargs):
    file_id = extract_drive_file_id(url)

    return pd.read_csv(
        f"https://drive.google.com/uc?id={file_id}",
        **kwargs,
    )


def google_excel_to_df(url, **kwargs):
    file_id = extract_drive_file_id(url)

    return pd.read_excel(
        f"https://drive.google.com/uc?id={file_id}",
        **kwargs,
    )


def google_sheet_to_df(url, **kwargs):
    sheet_id = extract_sheet_id(url)

    csv_url = (
        f"https://docs.google.com/spreadsheets/d/"
        f"{sheet_id}/export?format=csv"
    )

    return pd.read_csv(csv_url, **kwargs)