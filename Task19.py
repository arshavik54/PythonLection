# Задача №19. Дана последовательность из N целых чисел и число K. Необходимо
# сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо,
# K – положительное число.
# Input:   [1, 2, 3, 4, 5] k = 3
# Output:  [3, 4, 5, 1, 2]
# Примечание: Пользователь может вводить значения списка или список задан
# изначально.

from random import randint


list_1=[i  for i in range(1,randint(7,10))]
print(list_1)

k = int(input('Введите число: '))
#print(list_1.pop())

# for _ in range(k):
#     last_el = list_1.pop()
#     list_1.insert(0, last_el)
# print(list_1)

print(list_1[-k:] + list_1[:-k])