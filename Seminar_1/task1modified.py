

try:
    numbers = []
    for i in range(5):
        numbers.append(int(input(f'Введите число {i+1}: ')))
    max_num = numbers[0]
    min_num = numbers[0]
    index_max = 0
    index_min = 0
    sum = 0
    for i in range(len(numbers)):
        sum += numbers[i]
        if numbers[i] > max_num:
            max_num = numbers[i]
            index_max = i
        elif numbers[i] < min_num:
            min_num = numbers[i]
            index_min = i
    print('Максимальное число =', max_num, 'Индекс = ', index_max)
    print('Минимальное число =', min_num, 'Индекс = ', index_min)
    print('Среднее арифметическое = ', sum/len(numbers))
except:
    print('Введите целое число')
