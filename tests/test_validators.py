from google_data_utils.validators import extract_drive_file_id


def test_extract_drive_file_id():
    url = (
        "https://drive.google.com/file/d/"
        "ABC123/view?usp=sharing"
    )

    assert extract_drive_file_id(url) == "ABC123"