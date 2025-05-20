import pytest
from src.dateutils import DateUtils
from datetime import date, timedelta

def test_is_leap_year():
        current_year = date.today().year
        expected = current_year % 4 == 0 and (current_year % 100 != 0 or current_year % 400 == 0)
        assert DateUtils.is_leap_year(current_year) == expected

# Auto-generated tests (2025-05-20T18:53:40.413500)
def test_add_days_to_date_valid_input():
    start_date = date(2023, 9, 15)
    days = 5
    new_date = DateUtils.add_days_to_date(start_date, days)
    assert new_date == date(2023, 9, 20)

def test_add_days_to_date_negative_days():
    start_date = date(2023, 9, 15)
    days = -5
    new_date = DateUtils.add_days_to_date(start_date, days)
    assert new_date == date(2023, 9, 10)

def test_is_leap_year():
    assert DateUtils.is_leap_year(2020) is True
    assert DateUtils.is_leap_year(2021) is False

def test_days_between_dates():
    start_date = date(2023, 9, 15)
    end_date = date(2023, 9, 20)
    days = DateUtils.days_between_dates(start_date, end_date)
    assert days == 5

def test_get_weekday():
    test_date = date(2023, 9, 15)
    weekday = DateUtils.get_weekday(test_date)
    assert weekday == "Friday"

def test_time_until_next_holiday_valid_holidays():
    holidays = [(12, 25), (1, 1)]  # Christmas and New Year
    remaining_days = DateUtils.time_until_next_holiday(holidays)
    assert remaining_days.days >= 0

def test_time_until_next_holiday_no_holidays():
    with pytest.raises(ValueError):
        DateUtils.time_until_next_holiday([])

def test_time_until_next_holiday_invalid_holidays():
    invalid_holidays = [(2, 30), (4, 31)]  # Invalid dates
    with pytest.raises(ValueError):
        DateUtils.time_until_next_holiday(invalid_holidays)