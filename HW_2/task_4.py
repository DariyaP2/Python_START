"""
Задайте список из N элементов, заполненный целыми числами из промежутка [-N, N].
Найдите произведение элементов на индексах, хранящихся в файле indexes.txt (в одной строке один индекс).
Решение должно работать при любом натуральном N.

Ввод: значение типа <int>
Вывод: значение типа <int>

import random

f = open("file.txt")

input_num = 10
# input_num = int(f.readline(1))
# input_num = int(input('Введите число: '))
list = []

for i in range(input_num):
    list.append(random.randint(input_num*-1, input_num))

print(list)
result = 1

for line in f:
    print (list[int(line)], ' * ' , end='' )
    result = result * list[int(line)]

print('= ', result)

"""
