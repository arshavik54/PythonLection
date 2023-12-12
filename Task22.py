# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
#11 6
#2 4 6 8 10 12 10 8 6 4 2
#3 6 9 12 15 18
#6 12
#var1 = 5 5                         0.93 сек
var2 = "10 20 30 40 50"
var3 = "10 20 30 40 50"
list_symbols_2 = var2.split()
list_symbols_3 = var3.split()
list.sort(list_symbols_2)
print(list_symbols_2)
set_2 = set(list_symbols_2)
list.sort(list_symbols_3)
print(list_symbols_3)
set_3 = set(list_symbols_3)
set4 = set_2.intersection(set_3)
list_symbols_4 = list(set4)
list.sort(list_symbols_4)
print(*list_symbols_4)

#// 2      задействован var1                  0.11 сек
# mol = [int(x) for x in var1.split()]
# n = mol[0]
# m = mol[1]
# set_1 = set()
# set_2 = set()
# list_1 = list()
# a = [int(x) for x in var2.split()]
# k = set(a)
# for i in k:
#    set_1.add(i)
# b = [int(x) for x in var3.split()]
# k1 = set(b)
# for i in k1:
#    set_2.add(i)
# lok = set_1 & set_2
# kool = list(lok)
# kool.sort()
# for i in kool:
#    print(i, end=' ')

