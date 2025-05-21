import pytest
from src.dateutils import DateUtils
from datetime import date, timedelta

def test_is_leap_year():
        current_year = date.today().year
        expected = current_year % 4 == 0 and (current_year % 100 != 0 or current_year % 400 == 0)
        assert DateUtils.is_leap_year(current_year) == expected

# Auto-generated tests (2025-05-21T11:53:51.968028)
def test_add_days_to_date_valid_input():
    start_date = date(2022, 1, 1)
    days_to_add = 10
    new_date = DateUtils.add_days_to_date(start_date, days_to_add)
    assert new_date == date(2022, 1, 11)

def test_add_days_to_date_negative_days():
    start_date = date(2022, 1, 1)
    days_to_add = -5
    new_date = DateUtils.add_days_to_date(start_date, days_to_add)
    assert new_date == date(2021, 12, 27)

def test_is_leap_year():
    assert DateUtils.is_leap_year(2020) == True
    assert DateUtils.is_leap_year(2021) == False

def test_days_between_dates():
    start_date = date(2022, 1, 1)
    end_date = date(2022, 1, 10)
    days = DateUtils.days_between_dates(start_date, end_date)
    assert days == 9

def test_get_weekday():
    input_date = date(2022, 1, 1)
    weekday = DateUtils.get_weekday(input_date)
    assert weekday == "Saturday"

def test_time_until_next_holiday_valid_holidays():
    holidays = [(12, 25), (7, 4)]
    time_remaining = DateUtils.time_until_next_holiday(holidays)
    assert time_remaining.days > 0

def test_time_until_next_holiday_no_holiday():
    with pytest.raises(ValueError):
        DateUtils.time_until_next_holiday([])