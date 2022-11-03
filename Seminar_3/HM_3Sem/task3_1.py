# Задача 1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# def fill_list(number):
#     list = []
#     for i in range(number):
#         list.append(i)
#     return list

list = [2, 3, 5, 9, 3]


def odd_sum(list):
    sum = 0
    for i in range(len(list)):
        if (i % 2 != 0):
            sum += list[i]
    return sum

try:
    # number = int(input('Введите целое число: '))

    # print(f'Последовательность равна: {fill_list(number)}')
    print(f'Сумма элементов равна {odd_sum(list)}')

except:
    print('Введите целое число.')

