# 3. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.

# A = input("Введите строку 1: ")
# B = input("введите строку 2: ")
# count = 0
# if B in A: 
#     print("yes")

# for i in range (len(A) - len(B)):
#     if A[i:len(B)] == B:
#         count = count + 1
# print(count)



a = ["jnvfl", "dkkn", "lf", "dfdf"]
b = ["jnvfl", "dfdf"]
count = 0
for i in range (len(b)):
    if b[i] in a:
        count = count+1
        
print(count)


# def show_sequence(num):
#     for i in range(num):
#         print((-3) ** i, end=' ')
#     print()


# try:
#     n = int(input('Input N: '))
#     show_sequence(n)
# except ValueError:
#     print('Input real numbers!')
