import pytest
from src.dateutils import DateUtils
from datetime import date

def test_is_leap_year():
        current_year = date.today().year
        expected = current_year % 4 == 0 and (current_year % 100 != 0 or current_year % 400 == 0)
        assert DateUtils.is_leap_year(current_year) == expected

# Auto-generated tests (2025-05-20T16:49:33.383892)
def test_calculate_age():
    birth_date = date(1990, 5, 15)
    assert DateUtils.calculate_age(birth_date) == 31

def test_calculate_age_with_invalid_input():
    with pytest.raises(TypeError):
        DateUtils.calculate_age("1990-05-15")

def test_add_days_to_date():
    start_date = date(2021, 5, 1)
    new_date = DateUtils.add_days_to_date(start_date, 10)
    assert new_date == date(2021, 5, 11)

def test_add_days_to_date_with_invalid_input():
    with pytest.raises(TypeError):
        DateUtils.add_days_to_date("2021-05-01", 10)

def test_is_leap_year():
    assert DateUtils.is_leap_year(2020) == True
    assert DateUtils.is_leap_year(2021) == False

def test_is_leap_year_with_invalid_input():
    with pytest.raises(TypeError):
        DateUtils.is_leap_year("2020")

def test_days_between_dates():
    start_date = date(2021, 1, 1)
    end_date = date(2021, 1, 10)
    assert DateUtils.days_between_dates(start_date, end_date) == 9

def test_days_between_dates_with_invalid_input():
    with pytest.raises(TypeError):
        DateUtils.days_between_dates("2021-01-01", "2021-01-10")

def test_get_weekday():
    input_date = date(2021, 6, 15)
    assert DateUtils.get_weekday(input_date) == "Tuesday"

def test_get_weekday_with_invalid_input():
    with pytest.raises(TypeError):
        DateUtils.get_weekday("2021-06-15")

def test_time_until_next_holiday():
    holidays = [(12, 25), (7, 4)]  # Christmas and Independence Day
    time_until_holiday = DateUtils.time_until_next_holiday(holidays)
    assert time_until_holiday.days >= 0

def test_time_until_next_holiday_with_no_holidays():
    with pytest.raises(ValueError):
        DateUtils.time_until_next_holiday([])

def test_time_until_next_holiday_with_invalid_dates():
    holidays = [(2, 30)]  # Invalid February 30
    with pytest.raises(ValueError):
        DateUtils.time_until_next_holiday(holidays)