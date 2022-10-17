От Alexander Bashlaev всем 10:06 AM
А что за глюк?
От Bokovnev Evgeniy всем 10:06 AM
по предикатам?
От Olga всем 10:09 AM
А можно на семинаре разобрать конкретную задачу по предикатам, чтобы сложилось более четкое представление, как их решать?
От Timur Islamgulov всем 10:13 AM
b= True
a = True
not ( a and  b) = False
not(a) and not(b)
not(a) OR not(b)
for x in [True, False]:
От Militsa Voronina всем 10:16 AM
если в словаре в ключе элементы типа tuple , к этому ключу можно добавить новый элемент?
а поменять тип tuple на список в ключе можно?
От Alexander Bashlaev всем 10:16 AM
По-моему, нет
От Timur Islamgulov всем 10:23 AM
def summa_numbers(): #эта функця ничего не возвращает, только печатает на экран
    a=3
    b=6
    print(a+b)

#summa1()

def summa2(): #эта функця уже возвращает значение
    a=int(input("Введите первое число "))
    b=int(input("Введите второе число "))
    return a+b

#print(summa2())

x1=6
x2=5

def summa3(): #эта функця уже возвращает значение на основе глобальных переменных - не профессионально
    return x1 + x2

#print(summa3())
sum = 0

def summa4(): #эта функця изменяет глобальную переменную
    global sum
    a=int(input("Введите первое число "))
    b=int(input("Введите второе число "))
    sum = a + b

#summa4()
#print(sum)

def summa5(a,b): #эта функция уже принимает на вход аргументы и возвращает значение
    return a+b

try:
    a1=int(input("Введите первое число "))
    b1=int(input("Введите второе число "))
    print(summa5(a1, b1))
except:
    print("надо было вводить именно целое число")
