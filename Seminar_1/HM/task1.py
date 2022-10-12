# задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# *Пример:*
# - 6 -> да
# - 7 -> да
# - 1 -> нет

try:
    num = int(input("Put the number of the day of the week: "))

    list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if num > 5:
        print(f'{list[num - 1]} - day off')
    else:
        print(f'{list[num-1]} - working day')
except: 
    print("Put the correct number of the week day!")