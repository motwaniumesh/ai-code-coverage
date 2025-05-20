import pytest
from src.dateutils import DateUtils
from datetime import date

def test_is_leap_year():
        current_year = date.today().year
        expected = current_year % 4 == 0 and (current_year % 100 != 0 or current_year % 400 == 0)
        assert DateUtils.is_leap_year(current_year) == expected

# Auto-generated tests (2025-05-20T16:55:04.348404)
def test_add_days_to_date():
    start_date = date(2023, 1, 1)
    assert DateUtils.add_days_to_date(start_date, 5) == date(2023, 1, 6)
    
def test_is_leap_year():
    assert DateUtils.is_leap_year(2020) is True
    assert DateUtils.is_leap_year(2021) is False
    
def test_days_between_dates():
    start_date = date(2023, 1, 1)
    end_date = date(2023, 1, 10)
    assert DateUtils.days_between_dates(start_date, end_date) == 9
    
def test_get_weekday():
    input_date = date(2023, 1, 1)
    assert DateUtils.get_weekday(input_date) == "Sunday"
    
def test_time_until_next_holiday():
    holidays = [(1, 1), (12, 25)]  # New Year's Day and Christmas Day
    assert DateUtils.time_until_next_holiday(holidays) > timedelta(days=0)
    with pytest.raises(ValueError):
        DateUtils.time_until_next_holiday([])
    with pytest.raises(ValueError):
        DateUtils.time_until_next_holiday([(2, 30)])  # Invalid date