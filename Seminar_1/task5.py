# 3. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

def multiple(num):
    if (num % 5 == 0 and num % 10 == 0 or num % 15 == 0) and num % 30 != 0:
        print("Число удовлетворяет данным условиям")
    else:
        print("Число не удовлетворяет данным условиям")
try:
    num = int(input("Введите число: "))
    multiple(num)
except:
    print('Введите целое число')
