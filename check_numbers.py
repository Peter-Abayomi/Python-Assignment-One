def check_numbers(numbers):
    for item in numbers:
        if item % 2 == 0:
            print(item)
        else:
            print('There are no even number in this list')


values = [2, 5, 4, 6, 8, 10, 9, 7, 3, 11, 12, 13, 14, 16, 15, 17, 18, 16]

check_numbers(values)
