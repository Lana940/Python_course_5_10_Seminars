# Задача 5 Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры. Отсортировать элементы по возрастанию слева направо и сверху вниз.
# Например, задан массив:
# 1 4 7 2
# 5 9 10 3

# После сортировки
# 1 2 3 4
# 5 7 9 10

from random import randint

rows = int(input("Put number of rows: "))
cols = int(input("Put number of columns: "))

mass = [[randint(0, 10) for j in range(cols)] for i in range(rows)]
print(mass)

# mass2 = []

# for i in mass:
#     mass2.append(sorted(i))
# print(mass2)

x = len(mass[0])
y = len(mass)

list = []
for i in range(y):
    for j in mass[i]:
        list.append(j)
print(list)


max_num = 1
while max_num < len(list):
    for i in range(len(list) - max_num):
        if list[i] > list[i + 1]:
            list[i], list [i + 1] = list[i + 1], list[i]
            
    max_num +=1
print(list)

