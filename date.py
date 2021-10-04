from datetime import date


def date_subtraction(year_one, year_two):
    """Print the number of days between two dates"""
    days_between = (year_one - year_two)
    print(f"There are {days_between}days between {year_one} and {year_two}")


one = date(2019, 4, 13)
two = date(2017, 5, 15)

date_subtraction(one, two)
