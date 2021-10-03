def check_numbers(number):
    if bool(number) is False:
        print("The list is empty")
    elif bool(number) is True:
        for item in number:
            if isinstance(item, int) and item % 2 == 0:
                print(item)
            elif isinstance(item, str):
                print('There are no numbers in the list')


number = [2, 5, 4, 6, 8, 10, 9, 7, 3, 11, 12, 13, 14, 16, 15, 17, 18, 16]

check_numbers(number)

