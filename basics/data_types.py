"==========Переменные========"
# Переменная - это ссылки на ячейки памяти, где хранятся какие-то данные, для дальнейшего использования этих данных, при обращении к названию переменной

num1 = 10
num2 = 45

print(num1) # 10
print(num1+num2) # 10 + 45

"========Правила наименовывания переменных======="

a = 5 # по назнаяению
# 1num = 5 нельзя начинать название с чисел
# num-li1 = 5 нельзя использовать символы кроме _
# hello world = 6 нельзя использовать символы кроме _
# print = 10 нельзя называть переменные встроенными названиями


hello_world = 5 # snake case

helloWorld = 6 # camel case

hello_world = 10

# print(hello_world)

"========Ввод и вывод данных======="

# print - функция вывода данных в терминал
# input - функция ввода данных с терминала

number = input('введи любое число: ') # 123491230
print('Введенное число -', number) # 123491230


"==========Типы данных========="
# Типы данных делятся на 2 вида: изменяемые, неизменяемые
# Изменяемые: list(список), dict(словарь), set(множества)
# Неизменяемые: int, float, complex, str, tuple, bool, None

# Изменяемые
list_ = [1,2,3,4]
dict_ = {'a':1, 'b':2}
set_ = {1,2,3,4,4}

# Неизменяемые
int_ = 10
float_ = 0.5
str_ = "Hello world"
tuple_ = (1,2,3,4)
bool_1 = True
bool_0 = False
none_ = None

print('изменяемые типы', list_, dict_, set_)
print('неизменяемые типы', int_, float_, str_, tuple_, bool_1, bool_0, none_)