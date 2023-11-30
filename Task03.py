# Задача 3
# В некоторой школе решили набрать три новых математических класса
# и оборудовать кабинеты для них новыми партами. За каждой партой 
# может сидеть два учащихся. Известно количество учащихся в каждом из 
# трех классов. Выведите наименьшее число парт, которое нужно приобрести
# для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

import math

firstClassStudentsCount = int(input("Введите количество учеников 1 класса: "))
secondClassStundentsCount = int(input("Введите количество учеников 2 класса: "))
thirdClassStudentsCount = int(input("Введите количество учеников 3 класса: "))

#print(math.ceil(firstClassStudentsCount / 2) + math.ceil(secondClassStundentsCount / 2) + math.ceil(thirdClassStudentsCount / 2))

print((firstClassStudentsCount + 1) // 2 + (secondClassStundentsCount + 1) // 2 + (thirdClassStudentsCount + 1) // 2)