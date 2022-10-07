# Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
    
#     *Примеры:* 
    
#     - 5, 25 -> да
#     - 4, 16 -> да
#     - 25, 5 -> да
#     - 8,9 -> нет

try:
    number1 = int(input('Введите первое число: '))
    number2 = int(input('Введите второе число: '))
    if number1 ** 2 == number2:
        print(f'{number2} является квадратом числа {number1}')
    elif number2 ** 2 == number1:
        print(f'{number1} является квадратом числа {number2}')
    else:
        print('Ни одно из числе не является квадратом другого')
except:
    print('Введите целое число')




    # 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
    
    # Примеры:
    
    # - 1, 4, 8, 7, 5 -> 8
    # - 78, 55, 36, 90, 2 -> 90
def create_list():
    list = []
    for i in range(1,6):
        value = int(input("Vvedite chislo: "))
        list.append(value)
    return list


def find_max(list):
    max = list[0]
    for i in range(len(list)):
        if list[i] > max:
             max = list[i]
    return max

res = create_list()
print(res)    
max = find_max(res)        
print(f"Maksimalxnoe znachenie v liste ravno {max}")