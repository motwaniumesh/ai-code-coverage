import pytest
from src.dateutils import DateUtils
from datetime import date, timedelta

def test_is_leap_year():
        current_year = date.today().year
        expected = current_year % 4 == 0 and (current_year % 100 != 0 or current_year % 400 == 0)
        assert DateUtils.is_leap_year(current_year) == expected

# Auto-generated tests (2025-05-21T14:22:22.594220)
import pytest
from datetime import date, timedelta
from src.dateutils import DateUtils


def test_add_days_to_date_positive():
    start_date = date(2023, 5, 15)
    result = DateUtils.add_days_to_date(start_date, 10)
    assert result == date(2023, 5, 25)


def test_add_days_to_date_negative():
    start_date = date(2022, 12, 1)
    result = DateUtils.add_days_to_date(start_date, -10)
    assert result == date(2022, 11, 21)


def test_is_leap_year():
    assert DateUtils.is_leap_year(2020) == True
    assert DateUtils.is_leap_year(2021) == False


def test_days_between_dates():
    start_date = date(2022, 7, 15)
    end_date = date(2022, 8, 20)
    result = DateUtils.days_between_dates(start_date, end_date)
    assert result == 36


def test_get_weekday():
    input_date = date(2022, 5, 12)
    result = DateUtils.get_weekday(input_date)
    assert result == "Thursday"


def test_time_until_next_holiday_valid():
    holidays = [(12, 25), (7, 4)]  # Christmas and Independence Day
    result = DateUtils.time_until_next_holiday(holidays)
    assert isinstance(result, timedelta)


def test_time_until_next_holiday_empty_list():
    with pytest.raises(ValueError):
        DateUtils.time_until_next_holiday([])


def test_time_until_next_holiday_invalid_holidays():
    holidays = [(2, 30), (4, 31)]
    with pytest.raises(ValueError):
        DateUtils.time_until_next_holiday(holidays)