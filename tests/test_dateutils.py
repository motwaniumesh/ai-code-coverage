import pytest
from src.dateutils import DateUtils
from datetime import date

def test_is_leap_year():
        current_year = date.today().year
        expected = current_year % 4 == 0 and (current_year % 100 != 0 or current_year % 400 == 0)
        assert DateUtils.is_leap_year(current_year) == expected

# Auto-generated tests (2025-05-20T16:48:19.324673)
def test_calculate_age():
    birth_date = date(2000, 1, 1)
    assert DateUtils.calculate_age(birth_date) == (date.today().year - birth_date.year)

def test_calculate_age_invalid_input():
    with pytest.raises(TypeError):
        DateUtils.calculate_age("invalid")

def test_add_days_to_date():
    start_date = date(2022, 1, 1)
    days = 10
    assert DateUtils.add_days_to_date(start_date, days) == date(2022, 1, 11)

def test_add_days_to_date_negative_days():
    start_date = date(2022, 1, 15)
    days = -5
    assert DateUtils.add_days_to_date(start_date, days) == date(2022, 1, 10)

def test_add_days_to_date_invalid_input():
    with pytest.raises(TypeError):
        DateUtils.add_days_to_date("invalid", "invalid")

def test_is_leap_year():
    assert DateUtils.is_leap_year(2024) == True
    assert DateUtils.is_leap_year(2021) == False

def test_is_leap_year_invalid_input():
    with pytest.raises(TypeError):
        DateUtils.is_leap_year("invalid")

def test_days_between_dates():
    start_date = date(2022, 1, 1)
    end_date = date(2022, 1, 10)
    assert DateUtils.days_between_dates(start_date, end_date) == 9

def test_days_between_dates_invalid_input():
    with pytest.raises(TypeError):
        DateUtils.days_between_dates("invalid", "invalid")

def test_get_weekday():
    input_date = date(2022, 1, 1)
    assert DateUtils.get_weekday(input_date) == "Saturday"

def test_get_weekday_invalid_input():
    with pytest.raises(TypeError):
        DateUtils.get_weekday("invalid")

def test_time_until_next_holiday():
    holidays = [(12, 25), (11, 11)]
    next_holiday_timedelta = DateUtils.time_until_next_holiday(holidays)
    assert next_holiday_timedelta.total_seconds() > 0

def test_time_until_next_holiday_invalid_holidays():
    with pytest.raises(ValueError):
        DateUtils.time_until_next_holiday([])

def test_time_until_next_holiday_invalid_date_in_holidays():
    holidays = [(2, 30)]  # Invalid date
    with pytest.raises(ValueError):
        DateUtils.time_until_next_holiday(holidays)