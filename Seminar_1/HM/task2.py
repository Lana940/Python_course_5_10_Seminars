# задача 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input('x = '))
y = int(input('y = '))
z = int(input('z = '))

if not(x or y or z) == (not x and not y and not z):
    print(True)