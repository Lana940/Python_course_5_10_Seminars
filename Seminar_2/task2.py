# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
    
#     *Пример:*
    
#     - A (3,6); B (2,1) -> 5,09
#     - A (7,-5); B (1,-1) -> 7,21

import math

ax = float(input("Введите координату x точки A "))
ay = float(input("Введите координату y точки A "))
bx = float(input("Введите координату x точки B "))
by = float(input("Введите координату y точки B "))

distance = math.sqrt((bx - ax)**2 + (by - ay)**2)
# print(round(distance, 2))
print(distance "{:.2f}".format(5))


# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
import math
try:
    coordA = []
    for i in range(2):
        coordA.append(int(input("введите координату точки А: ")))
    coordB = []
    for i in range(2):
        coordB.append(int(input('введите координату точки В: ')))
    print(coordA, coordB)
    
    distan = math.sqrt((coordB[0]- coordA[0])**2 + (coordB[1]- coordA[1])**2)
    print(round(distan, 3))
except:
    print('Введите числа')

