# validators.py

from urllib.parse import urlparse
import re

class InvalidGoogleUrl(ValueError):
    pass


_DRIVE_FILE_RE = re.compile(
    r"^/file/d/([a-zA-Z0-9_-]+)"
)

_SHEET_RE = re.compile(
    r"^/spreadsheets/d/([a-zA-Z0-9_-]+)"
)

def is_google_drive_url(url: str) -> bool:
    try:
        extract_drive_file_id(url)
        return True
    except InvalidGoogleUrl:
        return False


def is_google_sheet_url(url: str) -> bool:
    try:
        extract_sheet_id(url)
        return True
    except InvalidGoogleUrl:
        return False
    
def extract_drive_file_id(url: str) -> str:
    """
    Accepts:
      https://drive.google.com/file/d/FILE_ID/view
    """

    parsed = urlparse(url)

    if parsed.netloc != "drive.google.com":
        raise InvalidGoogleUrl(
            "Expected a drive.google.com URL"
        )

    match = _DRIVE_FILE_RE.match(parsed.path)

    if not match:
        raise InvalidGoogleUrl(
            "Could not extract Drive file ID"
        )

    return match.group(1)


def extract_sheet_id(url: str) -> str:
    """
    Accepts:
      https://docs.google.com/spreadsheets/d/SHEET_ID/edit
    """

    parsed = urlparse(url)

    if parsed.netloc != "docs.google.com":
        raise InvalidGoogleUrl(
            "Expected a docs.google.com URL"
        )

    match = _SHEET_RE.match(parsed.path)

    if not match:
        raise InvalidGoogleUrl(
            "Could not extract Sheet ID"
        )

    return match.group(1)

def drive_download_url(url: str) -> str:
    file_id = extract_drive_file_id(url)
    return f"https://drive.google.com/uc?id={file_id}"

def sheet_csv_url(url: str) -> str:
    sheet_id = extract_sheet_id(url)
    return (
        f"https://docs.google.com/spreadsheets/d/"
        f"{sheet_id}/export?format=csv"
    )