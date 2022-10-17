

#  4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

def check_digit(text):
    check = False
    while not check:
        try:
            number = int(input(f"{text}"))
            check = True
        except ValueError as error:
            print(f"Пожалуйста, введите именно ЦЕЛОЕ число - {error}")
    return number

m = check_digit('Введите число:')
list1 = []
for i in range(-m,m):
    list1.append(i)
print(list1)


path = 'file.txt'
data = open(path, 'r')
prod = 1
for line in data:
    prod *= list1[int(line)]
print(prod)
data.close()
