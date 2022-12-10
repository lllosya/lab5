from pprint import pprint
list_ = list()  # Создаем пустой список

for i in range(0, 16):  # Перебираем все значение от 0 до 15 (верхняя граница не входит, пишем 16)
    num_ = {'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)}  # Создаем словарь для i-го числа
    list_.append(num_)  # Добавляем в список, созданный словарь

pprint(list_)
