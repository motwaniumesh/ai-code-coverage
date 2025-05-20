import pytest
from src.dateutils import DateUtils
from datetime import date, timedelta

def test_is_leap_year():
        current_year = date.today().year
        expected = current_year % 4 == 0 and (current_year % 100 != 0 or current_year % 400 == 0)
        assert DateUtils.is_leap_year(current_year) == expected

# Auto-generated tests (2025-05-20T20:05:01.021114)
def test_add_days_to_date():
    assert DateUtils.add_days_to_date(date(2023, 1, 1), 5) == date(2023, 1, 6)
    assert DateUtils.add_days_to_date(date(2023, 1, 1), -5) == date(2022, 12, 27)
    
def test_is_leap_year():
    assert DateUtils.is_leap_year(2000) == True
    assert DateUtils.is_leap_year(2004) == True
    assert DateUtils.is_leap_year(1900) == False
    assert DateUtils.is_leap_year(2021) == False
    
def test_days_between_dates():
    assert DateUtils.days_between_dates(date(2023, 1, 1), date(2023, 1, 5)) == 4
    assert DateUtils.days_between_dates(date(2023, 1, 5), date(2023, 1, 1)) == 4
    
def test_get_weekday():
    assert DateUtils.get_weekday(date(2023, 1, 1)) == "Sunday"
    
def test_time_until_next_holiday():
    holidays = [(1, 1), (12, 25)]
    assert DateUtils.time_until_next_holiday(holidays) == timedelta(days=48)
    
    with pytest.raises(ValueError):
        DateUtils.time_until_next_holiday([])