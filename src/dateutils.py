from datetime import date, timedelta
from typing import List, Tuple

class DateUtils:
    """Utility class for date-related calculations"""
    
    @staticmethod
    def add_days_to_date(start_date: date, days: int) -> date:
        """
        Add days to a given date.
        
        Args:
            start_date: Starting date
            days: Number of days to add (can be negative)
            
        Returns:
            New date after addition
        """
        if not isinstance(start_date, date):
            raise TypeError("start_date must be a date object")
        if not isinstance(days, int):
            raise TypeError("days must be an integer")
            
        return start_date + timedelta(days=days)

    @staticmethod
    def is_leap_year(year: int) -> bool:
        """
        Check if a year is a leap year.
        
        Args:
            year: Year to check
            
        Returns:
            True if leap year, False otherwise
        """
        if not isinstance(year, int):
            raise TypeError("year must be an integer")
            
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @staticmethod
    def days_between_dates(start_date: date, end_date: date) -> int:
        """
        Calculate the number of days between two dates.
        
        Args:
            start_date: First date
            end_date: Second date
            
        Returns:
            Absolute number of days between dates
        """
        if not all(isinstance(d, date) for d in (start_date, end_date)):
            raise TypeError("Both arguments must be date objects")
            
        return abs((end_date - start_date).days)

    @staticmethod
    def get_weekday(input_date: date) -> str:
        """
        Get the weekday name for a given date.
        
        Args:
            input_date: Date to check
            
        Returns:
            Full weekday name (e.g., "Monday")
        """
        if not isinstance(input_date, date):
            raise TypeError("input_date must be a date object")
            
        return input_date.strftime("%A")

    @staticmethod
    def time_until_next_holiday(holidays: List[Tuple[int, int]]) -> timedelta:
        """
        Calculate time until next occurrence of any given holiday.
        
        Args:
            holidays: List of (month, day) tuples representing annual holidays
            
        Returns:
            Timedelta until next holiday occurrence
            
        Raises:
            ValueError: If no valid holidays provided
        """
        if not holidays:
            raise ValueError("At least one holiday must be provided")
            
        today = date.today()
        next_holidays = []
        
        for month, day in holidays:
            try:
                current_year = date(today.year, month, day)
                next_occurrence = (
                    current_year if current_year >= today 
                    else date(today.year + 1, month, day)
                )
                next_holidays.append(next_occurrence)
            except ValueError:
                continue  # Skip invalid dates like February 30
                
        if not next_holidays:
            raise ValueError("No valid holidays found in the list")
            
        closest_holiday = min(next_holidays)
        return closest_holiday - today