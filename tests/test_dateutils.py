import pytest
from src.dateutils import DateUtils
from datetime import date, timedelta

def test_is_leap_year():
        current_year = date.today().year
        expected = current_year % 4 == 0 and (current_year % 100 != 0 or current_year % 400 == 0)
        assert DateUtils.is_leap_year(current_year) == expected

# Auto-generated tests (2025-05-20T18:50:01.800913)
def test_add_days_to_date():
    start_date = date(2022, 1, 1)
    assert DateUtils.add_days_to_date(start_date, 5) == date(2022, 1, 6)
    assert DateUtils.add_days_to_date(start_date, -5) == date(2021, 12, 27)

def test_is_leap_year():
    assert DateUtils.is_leap_year(2000) == True
    assert DateUtils.is_leap_year(1900) == False

def test_days_between_dates():
    start_date = date(2022, 1, 1)
    end_date = date(2022, 1, 10)
    assert DateUtils.days_between_dates(start_date, end_date) == 9

def test_get_weekday():
    input_date = date(2022, 1, 1)
    assert DateUtils.get_weekday(input_date) == "Saturday"

def test_time_until_next_holiday():
    holidays = [(1, 1), (12, 25)]  # New Year's Day and Christmas
    assert DateUtils.time_until_next_holiday(holidays).days > 0