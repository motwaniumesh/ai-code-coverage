import pytest
from src.dateutils import DateUtils
from datetime import date, timedelta

def test_is_leap_year():
        current_year = date.today().year
        expected = current_year % 4 == 0 and (current_year % 100 != 0 or current_year % 400 == 0)
        assert DateUtils.is_leap_year(current_year) == expected

# Auto-generated tests (2025-05-21T11:30:19.154427)
def test_add_days_to_date_valid_input():
    start_date = date(2022, 5, 1)
    new_date = DateUtils.add_days_to_date(start_date, 5)
    assert new_date == date(2022, 5, 6)
    
def test_add_days_to_date_negative_days():
    start_date = date(2022, 5, 10)
    new_date = DateUtils.add_days_to_date(start_date, -5)
    assert new_date == date(2022, 5, 5)
    
def test_is_leap_year():
    assert DateUtils.is_leap_year(2020) == True
    assert DateUtils.is_leap_year(2021) == False
    
def test_days_between_dates_valid_input():
    start_date = date(2022, 5, 1)
    end_date = date(2022, 5, 10)
    days_diff = DateUtils.days_between_dates(start_date, end_date)
    assert days_diff == 9
    
def test_get_weekday():
    input_date = date(2022, 5, 1)
    weekday_name = DateUtils.get_weekday(input_date)
    assert weekday_name == "Sunday"
    
def test_time_until_next_holiday_valid_input():
    holidays = [(12, 25), (7, 4)]  # Christmas and Independence Day
    time_until_holiday = DateUtils.time_until_next_holiday(holidays)
    assert isinstance(time_until_holiday, timedelta)

def test_time_until_next_holiday_no_holidays():
    with pytest.raises(ValueError):
        DateUtils.time_until_next_holiday([])

def test_time_until_next_holiday_invalid_dates():
    holidays = [(2, 30)]  # Invalid date
    with pytest.raises(ValueError):
        DateUtils.time_until_next_holiday(holidays)