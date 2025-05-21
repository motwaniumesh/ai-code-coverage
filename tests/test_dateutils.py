import pytest
from src.dateutils import DateUtils
from datetime import date, timedelta

def test_is_leap_year():
        current_year = date.today().year
        expected = current_year % 4 == 0 and (current_year % 100 != 0 or current_year % 400 == 0)
        assert DateUtils.is_leap_year(current_year) == expected

# Auto-generated tests (2025-05-21T11:46:18.044991)
def test_add_days_to_date():
    start_date = date(2022, 8, 1)
    assert DateUtils.add_days_to_date(start_date, 5) == date(2022, 8, 6)
    assert DateUtils.add_days_to_date(start_date, -5) == date(2022, 7, 27)
    
def test_is_leap_year():
    assert DateUtils.is_leap_year(2020) == True
    assert DateUtils.is_leap_year(2021) == False

def test_days_between_dates():
    start_date = date(2022, 8, 1)
    end_date = date(2022, 8, 10)
    assert DateUtils.days_between_dates(start_date, end_date) == 9

def test_get_weekday():
    input_date = date(2022, 8, 1)
    assert DateUtils.get_weekday(input_date) == "Monday"

def test_time_until_next_holiday():
    holidays = [(8, 15), (12, 25)]  # Assumption: Sample holiday dates
    assert DateUtils.time_until_next_holiday(holidays) == timedelta(days=14)