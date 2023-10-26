"=========== Comprehensions генераторы списка =============="
# comprehensions -  генератор, для создания некой последовательности используя цикл For в одну строчку

# результат for элемент in последовательность

# генератор - это иторируемый объект, который не хранит в себе польностью всю последовательность, а создает их когда требуется.

# print(comprehesions) # generation object
# for i in comprehesions:
#    print(i)


# next - функция, которая запрашивает у генератора текущий элемент и генератор создает элемент.

"=====Синтаксический сахар======="

# list_comprehesion = list( (i for i in range(1,6)) )
# print(list_comprehesion) # [1,2,3,4,5,]
# list_comprehesion = [1,2,3,4,5,]

# list_comprehesion = [i for i in range(1,6) if i%2==0]
# print(list_comprehesion) # [2,4]

# # с использованием comprehensions cоздать список не четных чисел в диапазоне от 1 до 100 включительрно.
# result = [i for i in range(1,101,2)] 
# result = [i for i in range(1,101) if i%2!=0]

# result = [i*2 for i in range(1,101) if i%2!=0]
# print(result) # [2,6,10]

# result = []
# for i in range(1,101,2):
#     result.append(i*2)



# с использованием comprehensions создать список из 5 строк 'hello'
['hello', 'hello', 'hello', 'hello', 'hello',]

# result = ['hello' for i in range(5)]
# print(result)


# result = []
# for i in range():
#     result.append('hello')
#     print(result)


# с использованием comprehensions создать список чисел в диапазоне от 1 до 100
# если число кратное 3 оставляет в списке fizz
# в ином случае оставляет число

[1,2,'fizz', 4,5,'fizz']
result = ['fizz' if i%3==0 else i for i in range(1,101)]
print(result)

result = []
for i in range(1,101):
    if i%3==0:
        result.append('fizz')
    else:
        result.append(i)




matrix = [
    [0,0,0],
    [1,1,1]
    [2,2,2]
]

# [0,0,0,1,1,1,2,2,2]

result = [j for i in matrix for j in i]
print(result)


result = []
for i in matrix:
    for j in i:
        result.append(j)
print(result)


"================Set comprehesion======================"

set_ = set()
for i in range(1,11):
    set_.add(i)
print(set_)


result = {i if i%2==0 else i*2 for i in range(1,21)}
print(result) # {2,4,6,...}


result = {i for i in range(1,11)}


# если условие находится в начале то это тернарные условия (добавляется оператор else)

# если условие в конце то это фильтрация (не добавляется else)


"===============Dict comprehensions========================="
{1:1, 2:4}
dict_ = {}
for i in range(1,11):
    dict_.update({i:i**2})
print(dict_)

result = {i:i**2 for i in range(1,11)}
print(result)

# дается список [1,1,2,2,2,4,4,4,4]
# надо посчитать количество значений в спискe
# и записать в словарь в качестве ключа число 
# в качестве значения количество повторений элемента {1:2, 2:3, 4:5}


list_ = [1,1,2,2,2,4,4,4,4]
dict_ = {}
for i in list_:
    dict_.update({i:list_.count(i)})
print(dict_)

# или 

dict_ = {i:list_.count(i) for i in list_}

dict_ = {'a':2, 'b':3}
dict_ = {key:val for key, val in dict_.items()}
print(dict_) # {2:'a', 3:'b'}


# дается словарь {'a':2, 'b':3}
# создать новый словарь в котором будет лежать 
# {'a':'четное', 'b':'нечетное'}


# простой способ решения
dict_ = {'a':2, 'b':3}
dict2 = {}
for k,v in dict_.items():
    if v%2==0:
        dict2.update({k:'четное'})
    else:
        dict2.update({k:'нечетное'})
print(dict2)

# в comprehesions будет выглядеть так:
dict2 = {k*2: 'четное' if v%2==0 else 'нечетное' for k,v in dict_.items()}
print(dict2)

