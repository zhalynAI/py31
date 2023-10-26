
"== Модули и пакеты=="

# модуль - любой файл с расширением .py
# пакет - набор модулей (внутри обязательно должен быть файл __init__.py)

# import math -> модуль
# import random -> модуль
# import intertools -> модуль

"== Работа с файлами =="

#file = open('test.txt', 'r')
#print(file.read())
# open - функция, который открывает файл в определенном режиме.


# r - read (только для чтения)
# w - write (только для записи)
# a - append (только для дозаписи, добавляет в конец)
# x - создает файл, но если существует такой файл выдаст ошибку.
# b - binary (в бинарном виде)
 
# ===============READ

#try:
    #file = open('test.txt', 'r')
    # # print(dir(file))
    # print(file.readable()) # True
    # print(file.writable()) # False
    # print(file.read())
    # print(file.tell())
    # file.seek(0) - показывает курсор (каретка)
    # print(file.line())
    # print(file.lines())
    # print(file.tell())
# finally:
#     file.close()

# ================WRITE
# (\n) опускает на следующею строку
# try: 
#     file = open('test.txt', 'w')
#     file.write('my name is Anton\n')
#     file.write('my name is Anton\n')
#     file.writelines(['Makers\n', 'bootcamp\n'])
# finally: 
#     file.close()

# ======APPEND (режим чтения'a')====
# try: 
#     file = open('test.txt', 'a')
#     file.write('\nhello')
#     file.seek(1000)
#     file.write('i am John\n')
# finally: 
#     file.close()



"==Контекстный менеджер=="

# with open('test.txt', 'r') as file:
#     print(file.read())

# with open('test.txt', 'a') as file: 
#     file.write('hello\n')

with open('ertay.py', 'x') as file:
    if file.writable():
        file.write('print("hello world")')

