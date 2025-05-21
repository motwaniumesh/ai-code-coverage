import pytest
from src.dateutils import DateUtils
from datetime import date, timedelta

def test_is_leap_year():
        current_year = date.today().year
        expected = current_year % 4 == 0 and (current_year % 100 != 0 or current_year % 400 == 0)
        assert DateUtils.is_leap_year(current_year) == expected

# Auto-generated tests (2025-05-21T14:40:51.328043)
def test_add_days_to_date():
    start_date = date(2022, 6, 15)
    assert DateUtils.add_days_to_date(start_date, 5) == date(2022, 6, 20)
    assert DateUtils.add_days_to_date(start_date, -5) == date(2022, 6, 10)

def test_is_leap_year():
    assert DateUtils.is_leap_year(2020) == True
    assert DateUtils.is_leap_year(2024) == True
    assert DateUtils.is_leap_year(1900) == False
    assert DateUtils.is_leap_year(2000) == True

def test_days_between_dates():
    start_date = date(2022, 6, 15)
    end_date = date(2022, 6, 25)
    assert DateUtils.days_between_dates(start_date, end_date) == 10

def test_get_weekday():
    input_date = date(2022, 6, 15)
    assert DateUtils.get_weekday(input_date) == "Wednesday"

def test_time_until_next_holiday():
    holidays = [(12, 25), (7, 4)]  # Christmas and Independence Day
    assert DateUtils.time_until_next_holiday(holidays).days > 0