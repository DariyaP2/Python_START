"""
Напишите программу, которая принимает на вход натуральное число N и выдает список факториалов по основаниям от 1 до N

Ввод: значение типа <int>
Вывод: значение типа <list>

Пример:
4
[1, 2, 6, 24]

input_num = int(input('Введите число: '))
list = [1]

for i in range (1,input_num):
    list.append ((i+1) * list [i-1])

print(list)


#либо чеез переменную а не список
temp_num = 1
for i in range (input_num):
    temp_num *= i+1
    print(temp_num, end=' ')

print ()

"""
