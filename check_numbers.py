def check_numbers(number):
    if isinstance(number, list) == 0:
        return "This is not a list"
    if bool(number) is False:
        return "The list is empty"
    for item in number:
        if not isinstance(item, int):
            return "List contains no numbers"
    number_list = []
    for item in number:
        if item % 2 == 0:
            number_list.append(item)
    return('There are no even numbers' if bool(number_list) is False else number_list)


list_of_number = [2, 3, 5, 7, 8, 4, 6, 12, 13, 14, 15, 16, 1, 17, 18, 20, 21]

print(check_numbers(list_of_number))
