def calculate_days(year_one, month_one, day_one, year_two, month_two, day_two):
    subtraction = ((year_one - year_two) * 365) + ((month_one - month_two) * 30) + (day_one - day_two)
    print(f"The difference between {year_one}/{month_one}/{day_one} and {year_two}/{month_two}/{day_two} is {subtraction}days")


calculate_days(1999, 5, 2, 1998, 5, 6)
