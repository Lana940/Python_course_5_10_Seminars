# 3. Задайте список из n чисел последовательности (1+1/N)**N и выведите на экран их сумму.
    
def list_posl(number):
    list = []
    for i in range(1, number + 1):
        list.append(round((1 + 1 / i) ** i, 3))
    return list

def sum_values_list(list):
    sum = 0
    for i in list:
        sum += i
    return sum

try:
    num = int(input('Введите целое число: '))

    print(f'Последовательность равна: {list_posl(num)}')
    print(f'Сумма элементов равна {sum_values_list(list_posl(num))}')


except:
    print('Введите целое число.')
