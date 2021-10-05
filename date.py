from datetime import date


def date_subtraction(year_one, year_two):
    """Print the number of days between two dates"""
    try:
        year_one = date.fromisoformat("2019-12-13")
        year_two = date.fromisoformat("2017-05-15")
    except ValueError:
        print("The date format should be in YYYY-MM-DD format")
    else:
        days_between = (year_one - year_two)
        print(f"There are {days_between}days between {year_one} and {year_two}")


one = date(2019, 4, 13)
two = date(2017, 5, 15)

date_subtraction(year_one=one, year_two=two)
