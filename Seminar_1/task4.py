# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
    
#     *Примеры:*
    
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3

# number = float(input("Input number: "))
# number *= 10
# print(number)
# number = int(number)
# print(number)
# print(number % 10)


try:
    x = float(input('enter x:'))
    if int(x) - x == 0:  # проверка на ввод целого числа
        print('no')    
    else:
        print(int(x * 10 % 10))
except:
     print('enter numbers')
