import pytest
from src.dateutils import DateUtils
from datetime import date, timedelta

def test_is_leap_year():
        current_year = date.today().year
        expected = current_year % 4 == 0 and (current_year % 100 != 0 or current_year % 400 == 0)
        assert DateUtils.is_leap_year(current_year) == expected

# Auto-generated tests (2025-05-20T18:51:58.032751)
def test_add_days_to_date_valid_date():
    start_date = date(2023, 1, 1)
    days = 10
    assert DateUtils.add_days_to_date(start_date, days) == date(2023, 1, 11)

def test_add_days_to_date_negative_days():
    start_date = date(2023, 1, 10)
    days = -5
    assert DateUtils.add_days_to_date(start_date, days) == date(2023, 1, 5)

def test_is_leap_year():
    assert DateUtils.is_leap_year(2020) == True
    assert DateUtils.is_leap_year(2100) == False

def test_days_between_dates():
    start_date = date(2023, 1, 1)
    end_date = date(2023, 1, 11)
    assert DateUtils.days_between_dates(start_date, end_date) == 10

def test_get_weekday():
    input_date = date(2023, 1, 1)
    assert DateUtils.get_weekday(input_date) == "Sunday"

def test_time_until_next_holiday_valid():
    holidays = [(12, 25), (7, 4)]
    assert DateUtils.time_until_next_holiday(holidays) == timedelta(days=123)
    
def test_time_until_next_holiday_no_holidays():
    with pytest.raises(ValueError):
        DateUtils.time_until_next_holiday([])

def test_time_until_next_holiday_invalid_holidays():
    holidays = [(2, 30), (14, 50)]
    with pytest.raises(ValueError):
        DateUtils.time_until_next_holiday(holidays)