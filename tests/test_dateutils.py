import pytest
from src.dateutils import DateUtils
from datetime import date, timedelta

def test_is_leap_year():
        current_year = date.today().year
        expected = current_year % 4 == 0 and (current_year % 100 != 0 or current_year % 400 == 0)
        assert DateUtils.is_leap_year(current_year) == expected

# Auto-generated tests (2025-05-21T14:25:23.118781)
def test_add_days_to_date():
    start_date = date(2022, 1, 1)
    
    # Positive days
    assert DateUtils.add_days_to_date(start_date, 10) == date(2022, 1, 11)
    
    # Negative days
    assert DateUtils.add_days_to_date(start_date, -10) == date(2021, 12, 22)

def test_is_leap_year():
    assert DateUtils.is_leap_year(2000)
    assert DateUtils.is_leap_year(2020)
    assert not DateUtils.is_leap_year(1900)
    assert not DateUtils.is_leap_year(2021)

def test_days_between_dates():
    start_date = date(2022, 1, 1)
    end_date = date(2022, 1, 10)
    
    assert DateUtils.days_between_dates(start_date, end_date) == 9

def test_get_weekday():
    test_date = date(2022, 1, 1)
    
    assert DateUtils.get_weekday(test_date) == "Saturday"

def test_time_until_next_holiday():
    holidays = [(1, 1), (12, 25)]  # New Year's Day and Christmas
    
    assert DateUtils.time_until_next_holiday(holidays) > timedelta(days=0)

    with pytest.raises(ValueError):
        DateUtils.time_until_next_holiday([])

    with pytest.raises(ValueError):
        DateUtils.time_until_next_holiday([(2, 30)])