# задача 4 Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число, 
#         второе число и операцию, после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.

# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.

# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".


try:
    num1 = float(input("Put num1: "))
    num2 = float(input("Put num2: "))
    operation = input("Put the type of operation: ")

    if operation == '+':
        print(num1 + num2)
    if operation == '-':
        print(num1 - num2)
    if operation == '/'  and num2 == 0:
        print("Division by zero!")
    if operation == '/'  and num2 != 0:
        print(num1/num2)
    if operation == '*':
        print(num1*num2)
    if operation == 'mod':
        print(num1%num2)
    if operation == 'pow':
        print(num1**num2)
    if operation == 'div' and num2 == 0:
        print("Division by zero!")
    if operation == 'div' and num2 != 0:
        print(num1//num2)
except:
    print("Put number!")
    

