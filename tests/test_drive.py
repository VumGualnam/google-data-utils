import pytest

from google_data_utils.validators import (
    InvalidGoogleUrl,
    extract_drive_file_id,
    is_google_drive_url,
    drive_download_url,
)


def test_extract_drive_file_id():
    url = (
        "https://drive.google.com/file/d/"
        "ABC123_XYZ/view?usp=sharing"
    )

    assert extract_drive_file_id(url) == "ABC123_XYZ"


def test_extract_drive_file_id_invalid_domain():
    url = (
        "https://example.com/file/d/"
        "ABC123/view"
    )

    with pytest.raises(InvalidGoogleUrl):
        extract_drive_file_id(url)


def test_extract_drive_file_id_invalid_path():
    url = "https://drive.google.com/"

    with pytest.raises(InvalidGoogleUrl):
        extract_drive_file_id(url)


def test_is_google_drive_url_valid():
    url = (
        "https://drive.google.com/file/d/"
        "ABC123/view"
    )

    assert is_google_drive_url(url) is True


def test_is_google_drive_url_invalid_domain():
    url = (
        "https://example.com/file/d/"
        "ABC123/view"
    )

    assert is_google_drive_url(url) is False


def test_is_google_drive_url_invalid_path():
    url = "https://drive.google.com"

    assert is_google_drive_url(url) is False
    

def test_drive_download_url():
    url = (
        "https://drive.google.com/file/d/"
        "ABC123/view"
    )
    assert (
        drive_download_url(url)
        == "https://drive.google.com/uc?id=ABC123"
    )