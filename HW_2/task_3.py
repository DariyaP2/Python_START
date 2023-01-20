"""
Задайте список размерностью N. Каждый элемент списка вычисляется выражением (1 + 1 / n) ** n,
где n – позиция (не индекс) элемента в списке, причем 1 < n < N.
Выведите сумму элементов списка. Ответ округлите до сотых.

Ввод: значение типа <int>
Вывод: значение типа <float>

Пример:
1
2.0

2
4.25

3
6.62

from fractions import Fraction


input_num = int(input('Введите число: '))

list = []
sum = 0
for n in range(1,input_num+1):
    a = (1 + Fraction (1,n))**n
    sum += a #я не стал сумму делать отдельно, это будет просто пробегание по списку
    list.append (a)
print (sum)

print ('\nили')
list = [[],[]]
for n in range(1,input_num+1): #создание списка
    x = 1
    y = n
    x = x+1*y
    x = x**n
    y = y**n
    list[0].append(x)
    list[1].append(y)

for i in range(input_num): #сложение
    if i == 0:
        sum_x = list[0][i]
        sum_y = list[1][i]
    else:
        sum_x = sum_x * list[1][i] + sum_y * list[0][i]
        sum_y *= list[1][i]

print (sum_x,'/',sum_y)

print ('\nили')
sum = 0
for n in range(1,input_num+1):
    sum += (1+1/n)**n
print(sum)

"""
