"==Кортежи=="
# #Кортеж - неизменяемый, индексируемый, упорядоченный, итеруремый тип данных, предназначенный для хранения любых данных в определенном порядке. 

# tuple1 = (1,2,3,4, 'hello', [1,2], {'a','b'}, False, None)
# tuple1[0] # 1
# tuple1[4][2] # 1

# "==Методы Кортежей=="

# print(dir(tuple))
# # 
# # count
# tuple1 = (1,2,3,4,5,1,2,3,3,2)
# print(tuple1.count(1)) # 2
# print(tuple1.count(7)) # 0

# # index - возвращает индекс первого попавшегося элемента.
# tuple1(1,2,3,4,5,1,2,3,3,2)
# print(tuple1.index(1,4,8)) # 5
# tuple1[-1] # 2

# "==Set--Множества=="
# # множества - изменяемый, неупорядоченный, неиндексируемый, итерируемый тип данных, предназначенный для хранения уникальных данных (множества могут хранить только неизменяемые типы данных)

# set_ = {1,2,3,4,5,6} # {,}

# # print(type(a)) # dict

# set_ = set() # {} - множества
# set_ = {'hello', 1,2, 'hello'}
# # print(set_[0]) # Error

# for i in set_:
#     print(i)

# print('hello' in set_) # True
# print('hell' in set_) # Falsee


a = {'askjk', 'hello', 'chakjkd'}
# dist_  = {"a" : 5, (1,(1)):'hello'}
# print(dist_)

"=============Методы множеств============="
# add - добавляет элемент в set
set_ = {1,2,3}
set_.add(4)
set_.add('a')
# print(set_) # {1,2,3,4,'a'}

# pop - удаляет элемент по принципу FIFO)
set_ = {1,2,3,4}

popped = set_.pop()
print(set_, popped) # {'aasdf',2,3,4} 1

# remove -удаляет по значению 
set_ = {'aasdf', 1,2,3,4}
set_.remove('aasdf')
print(set_)

# intersection - находит пересечния между set и другими коллекциями (&)
set1 = {1,2,3,4}
set2 = {3,4,5,6}
set2 = list(set2)
print(set1.intersection(set2)) # {3,4}
print(set1 & set2) # Error

# difference - находит отличия относительно первого set (-)
set1 = {1,2,3,4}
set2 = {3,4,5,6}
print (set1.difference(set2)) # {1,2}
# print (set2.difference(set1)) # {5,6}
print(set1-set2) # Error

# symetric_difference - находит все отличия между set1 и set2
set1 = {1,2,3,4}
set2 = {3,4,5,6}
print (set1.symetric_difference(set2)) # {1,2,5,6}

# symetric_difference_update - обновит set1
set1 = {1,2,3,4}
set2 = {3,4,5,6}
print (set1.symetric_difference(set2)) # {1,2,5,6}

print(set1) # {1,2,5,6}

# discard - удаляет по значению если нет такого элемента не выдает ошибку.
set1 = {1,2,3,4}
discarded = set1.discard(5)
print(set1)

# union, issubset,issuperset - что делает эти методы?