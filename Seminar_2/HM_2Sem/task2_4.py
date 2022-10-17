# Задача 4 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу, которая принимает на вход N, и координаты двух точек и находит расстояние между ними в N-мерном пространстве.

Доделать!

import numpy as np

N = int(input("Введите число N: "))

vector1 = int(input(np.array([])))
vector2 = int(input(np.array([])))
 
op1=np.sqrt(np.sum(np.square(vector1-vector2)))
print(op1)



