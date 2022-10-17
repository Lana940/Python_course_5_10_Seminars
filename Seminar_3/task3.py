

# 20. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

def create_string_list(number):
    list = []
    for i in range(number):
        list.append(input('Введите что-нибудь: '))
    return list

def check_value_in_list(list, number):
    for i in list:
        if i == number:
            print('В списке присутствует ваше число!')

try:
    num = input('Введите искомое число: ')
    size = int(input('Введите размер списка: '))
    list = create_string_list(size)
    check_value_in_list(list, num)

except:
    print('Некорректный ввод!')
