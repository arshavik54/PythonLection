# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит число N - количество 
# элементов в первом массиве, затем N чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)

from random import randint

size_1 = int(input('Введите размер первого массива: '))
size_2 = int(input('Введите размер второго массива: '))

list_1 = []

# for i in range(size_1):
#     num = randint(0, 5)
#     list_1.append(num)

list_1 = [randint(0, 5) for i in range(size_1)]

print(list_1)


list_2 = []

# for i in range(size_2):
#     num = randint(0, 5)
#     list_2.append(num)

list_2 = [randint(0, 5) for i in range(size_2)]

print(list_2)

set_2 = set(list_2)

for el in list_1:
    if el not in set_2:
        print(el, end = ' ')