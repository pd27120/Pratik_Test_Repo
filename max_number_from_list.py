"""Find largest number in a list."""

number_list = [22, 44, 66, 999, 1100]


def max_number(list1):
    maximum = list1[0]
    for i in list1:
        if i > maximum:
            maximum = i
    return maximum


largest = max_number(number_list)
print(largest)
