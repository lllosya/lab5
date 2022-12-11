import random


def get_unique_list_numbers(x, y, n) -> list[int]:
    list_ = []
    while len(list_) < n:
        unique_num = random.randint(x, y)
        if unique_num in list_:
            continue
        else:
            list_.append(unique_num)
    return list_


list_unique_numbers = get_unique_list_numbers(-10, 10, 15)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
