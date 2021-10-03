def check_numbers(numbers):
    for item in numbers:
        if item % 2 == 0:
            print(item)
        else:
            print('There are no even number in this list')


values = [1, 5, 7, 5, 3]

check_numbers(values)
