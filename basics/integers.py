"==========Числа========="
# integers(int) - целые числа

# soft engineer

# PEP8

num: int = 5 #IDE

print(type(num)) # <class 'int'>

num1 = '10'
num1 = int(num1) # convert to integer object
print(type(num1)) # return type int

# float - вещественные числа (с плавающей точкой, десятичные)

a = 10.5
print(type(a)) # <class 'float'>

b = float(23)
print(b) # 23.0

c = float('45.9')
print(type(c)) # <class 'float'>

print(0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1) 

# decimal - точное вещественное число. Чтобы использовать decimal, нужно его импортировать

from decimal import Decimal

a = Decimal("0.1")

print(a*8)

# 7.001

"===========Операции над числами============"

5 + 7 # сложение
10 - 5 # вычитание
2 * 4 # умножение
15 / 3 # деление 5.0
15 // 3 # деление 5
5 % 2 # остаток от деления 1
2**3 # возведение в степень 8
25**0.5 # нахождение кв корня числа 5

# abs модуль числа - из отрицательного числа получаем положительное |-5| = 5

print(abs(-5)) # 5
print(abs(10)) # 10
print(abs(-0.1)) # 0.1

# round - округление числа

print(round(5.6)) # 6
print(round(5.5)) # 6 (округление в большую сторону)
print(round(5.49)) # 5 (округление идет только по первой цифре после точки)

print(round(10 / 3, 1)) # 3.3
print(round(10.0007852, 4)) # 10.0008
print(round(10.0476, 2)) # 10.05
print(round(10.0478, 3)) # 10.048

# sqrt - функция для нахождения кв корня числа, его нужно импортировать

from math import sqrt
print(sqrt(25)) # 5.0
print(sqrt(36)) # 6.0
print(sqrt(34)) # 5.830951894845301

# pow
# 1. возводит в степень
# 2. нахoдит остаток от деления на 3 число

print(pow(2, 3)) # 2**3 = 8
print(pow(2, 3, 4)) # 2**3%4 = 0

# divmod - функция, которая возвращает 2 числа, где 1 - целая часть от деления, 2 - остаток от деления
print(divmod(5, 2)) # 5//2, 5%2 = 2, 1
print(divmod(17, 3)) # 5, 2

