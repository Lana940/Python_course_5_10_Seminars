

# 21. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

# *Пример:*

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

def create_string_list(number):
    list = []
    for i in range(number):
        list.append(input('Введите что-нибудь: '))
    return list

def check_double_first_value(list, find):
    check = 0
    find_index = -1
    for i in range(len(list)):
        if list[i] == find:
            check += 1
        if check == 2:
            find_index = i
            break

    return find_index

size = int(input('Введите размер списка: '))
list = create_string_list(size)
find = input('Ищем: ')
if check_double_first_value(list, find) == (-1):
    print('Нет повторов')
else:
    print(f'Искомый элемент стоит на {check_double_first_value(list,find)} позиции.')
