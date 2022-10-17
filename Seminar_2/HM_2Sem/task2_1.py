
# Задача 1. Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр. Через строку нельзя решать.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11

# через строку:

# n = input('Введите число: ')
# sum = 0

# for digit in n:
#     if digit.isdigit():
#         sum += int(digit)


# print(f'Сумма цифр = {sum}')


# для целого числа:

def sum_of_digits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum

print(sum_of_digits(66)) 

