# Задача №17. Дан список чисел. Определите, сколько в нем встречается различных 
# чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения списка или список задан
# изначально.

from random import randint


size = int(input('введите размер списка: '))
#list_1 = []
# for _ in range(size):
#     list_1.append(randint(-5,5))
    
list_2 = [randint(-5,5) for _ in range(size)]
print(list_2)
# unique_nums = set(list_2)
# print(len(unique_nums))
print(len(set(list_2)))
#print(len(set([randint(-5,5) for _ in range(size)])))
