def check_numbers(number):
    if number:
        for item in number:
            if isinstance(item, int) and item % 2 == 0:
                print(item)
            elif isinstance(item, str):
                print('There are no numbers in the list')
    else:
        print("The list is empty")


number = [2, 5, 4, 6, 8, 10, 9, 7, 3, 11, 12, 13, 14, 16, 15, 17, 18, 16]

check_numbers(number)

