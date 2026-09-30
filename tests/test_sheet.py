# tests/test_sheet.py

import pytest

from google_data_utils.validators import (
    InvalidGoogleUrl,
    extract_sheet_id,
    is_google_sheet_url,
)


def test_extract_sheet_id():
    url = (
        "https://docs.google.com/spreadsheets/d/"
        "ABC123_XYZ/edit#gid=0"
    )

    assert extract_sheet_id(url) == "ABC123_XYZ"


def test_extract_sheet_id_export_url():
    url = (
        "https://docs.google.com/spreadsheets/d/"
        "ABC123_XYZ/export?format=csv"
    )

    assert extract_sheet_id(url) == "ABC123_XYZ"


def test_extract_sheet_id_invalid_domain():
    url = (
        "https://example.com/spreadsheets/d/"
        "ABC123/edit"
    )

    with pytest.raises(InvalidGoogleUrl):
        extract_sheet_id(url)


def test_extract_sheet_id_invalid_path():
    url = "https://docs.google.com/spreadsheets"

    with pytest.raises(InvalidGoogleUrl):
        extract_sheet_id(url)


def test_is_google_sheet_url_valid_edit():
    url = (
        "https://docs.google.com/spreadsheets/d/"
        "ABC123/edit"
    )

    assert is_google_sheet_url(url) is True


def test_is_google_sheet_url_valid_export():
    url = (
        "https://docs.google.com/spreadsheets/d/"
        "ABC123/export?format=csv"
    )

    assert is_google_sheet_url(url) is True


def test_is_google_sheet_url_invalid_domain():
    url = (
        "https://example.com/spreadsheets/d/"
        "ABC123/edit"
    )

    assert is_google_sheet_url(url) is False


def test_is_google_sheet_url_invalid_path():
    url = "https://docs.google.com/spreadsheets"

    assert is_google_sheet_url(url) is False