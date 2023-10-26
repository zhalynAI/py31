# if else
# list 
# dict
# for 

#  вам дается строка "hello world i am alive"
# надо подсчитать количество гласных букв
string = "hello world i am alive"
counter = 0
vowels = 'auioy'
for letter in string:
    if letter in vowels: 
         counter+=1 # ( или можно так counter = +1)
                 
print(counter)

list_ = [1,2,3,4,5,7,9,0]
list2 = []
for i in list_:
     list2.append(i//2)
     print(list2)
print(sum(list_))  # 31

# вам дан список ['hello', 1,2,3,6,8,'fgh', False, None]
# создать список и добавить только числа
# [1,2,3,6,8]

list_ = ['hello', 1,2,3,6,8,'fgh', False, None]
list2 = []
for val in list_:
     if type(val) == int:
          list2.append(val)
print(list2)     

'logical operetions'
# task 11
num = int(input())
chr(num)
if chr(num).isalha():
     print(f'Это не буква, а символ \" а символ "символ"')

# task 16 разбор
a = int(input())
b = int(input())
c = int(input())

if a < b:
     if b < c:
          print(a, b, c) 
     elif c < a:
          print(c, a, b)
     else:
          print(a, c, b)
elif a < c:
     print(b, a, c)
elif c < b:
     print(c, b, a)

else:
     print(b, c, a)

'lists'
# task 18
 
last_names = []
# ['ertay', 'esenbekov']
last_name = input().split()[-1]
last_names.append(last_name)
last_name = input().split()[-1]
last_names.append(last_name)
last_name = input().split()[-1]
last_names.append(last_name)
last_name = input().split()[-1]
last_names.append(last_name)
last_name = input().split()[-1]
last_names.append(last_name)
 

# task 8
list_ = [1,2,3,4,5]
new_list = []
for val in list_:
     new_list.append(str(val))
print(new_list)

# task 24 

size = 3 
#[]
#   [1,2,3],
#   [1,2,3],
#   [1,2,2]
#]
size = 6 
list_ = []
inner_list = list(range(1, size+1))

for i in range(size):
     list_.append(inner_list)

print(list_)


# Списка 
# task30 
# Создайте список с 3 вложенными списками, где внутри должно быть три 0 K = 3 (количество списков и элементов)
# Результат 