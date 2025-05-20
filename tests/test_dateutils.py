import pytest
from src.dateutils import DateUtils
from datetime import date, timedelta

def test_is_leap_year():
        current_year = date.today().year
        expected = current_year % 4 == 0 and (current_year % 100 != 0 or current_year % 400 == 0)
        assert DateUtils.is_leap_year(current_year) == expected

# Auto-generated tests (2025-05-20T18:43:46.308737)
def test_add_days_to_date():
    start_date = date(2022, 1, 1)
    assert DateUtils.add_days_to_date(start_date, 5) == date(2022, 1, 6)
    
def test_is_leap_year():
    assert DateUtils.is_leap_year(2020) is True
    assert DateUtils.is_leap_year(1900) is False
    
def test_days_between_dates():
    start_date = date(2022, 1, 1)
    end_date = date(2022, 1, 10)
    assert DateUtils.days_between_dates(start_date, end_date) == 9
    
def test_get_weekday():
    input_date = date(2022, 1, 1)
    assert DateUtils.get_weekday(input_date) == "Saturday"
    
def test_time_until_next_holiday():
    holidays = [(1, 1), (7, 4)]  # New Year's Day, Independence Day
    expected_delta = timedelta(days=104)  # Days until Independence Day
    assert DateUtils.time_until_next_holiday(holidays) == expected_delta

def test_add_days_to_date_invalid_input():
    with pytest.raises(TypeError):
        DateUtils.add_days_to_date("2022-01-01", 5)

def test_is_leap_year_invalid_input():
    with pytest.raises(TypeError):
        DateUtils.is_leap_year("2020")

def test_days_between_dates_invalid_input():
    with pytest.raises(TypeError):
        DateUtils.days_between_dates("2022-01-01", "2022-01-10")
    
def test_get_weekday_invalid_input():
    with pytest.raises(TypeError):
        DateUtils.get_weekday(2022)
    
def test_time_until_next_holiday_no_holidays():
    with pytest.raises(ValueError):
        DateUtils.time_until_next_holiday([])