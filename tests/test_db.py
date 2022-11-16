import pytest
from app.db import DateFormatValidator


@pytest.fixture
def date_format_validator():
    return DateFormatValidator


def test_date_format_validator_correct_date(date_format_validator):
    assert date_format_validator().is_data_correct('2020-09-09') == True


def test_date_format_validator_incorrect_date(date_format_validator):
    assert date_format_validator().is_data_correct('2020-13-09') == False


def test_date_format_validator_incorrect_format(date_format_validator):
    assert date_format_validator().is_data_correct('03-09-2020') == False


