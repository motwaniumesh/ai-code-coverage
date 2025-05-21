import pytest
from src.dateutils import DateUtils
from datetime import date, timedelta

def test_is_leap_year():
        current_year = date.today().year
        expected = current_year % 4 == 0 and (current_year % 100 != 0 or current_year % 400 == 0)
        assert DateUtils.is_leap_year(current_year) == expected

# Auto-generated tests (2025-05-21T14:11:38.091004)
from datetime import date, timedelta
from typing import List, Tuple
import pytest
from src.dateutils import DateUtils

def test_add_days_to_date():
    start_date = date(2022, 1, 1)
    assert DateUtils.add_days_to_date(start_date, 5) == date(2022, 1, 6)
    assert DateUtils.add_days_to_date(date(2021, 12, 31), 1) == date(2022, 1, 1)

def test_is_leap_year():
    assert DateUtils.is_leap_year(2000) == True
    assert DateUtils.is_leap_year(2100) == False

def test_days_between_dates():
    start_date = date(2022, 1, 1)
    end_date = date(2022, 1, 5)
    assert DateUtils.days_between_dates(start_date, end_date) == 4

def test_get_weekday():
    input_date = date(2022, 1, 1)
    assert DateUtils.get_weekday(input_date) == 'Saturday'

def test_time_until_next_holiday():
    holidays = [(1, 1), (7, 4)]  # New Year's Day and Independence Day
    assert DateUtils.time_until_next_holiday(holidays) == timedelta(days=184)

    with pytest.raises(ValueError):
        DateUtils.time_until_next_holiday([])

    with pytest.raises(ValueError):
        DateUtils.time_until_next_holiday([(2, 30)])