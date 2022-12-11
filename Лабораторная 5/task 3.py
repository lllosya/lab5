import random


def get_unique_list_numbers(x, y, n) -> list[int]:
    while True:
        unique_num = [random.randint(x, y) for _ in range (n)]
        if len(unique_num) == len(set(unique_num)):
            return unique_num
        else:
            continue


list_unique_numbers = get_unique_list_numbers(-10, 10, 15)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
