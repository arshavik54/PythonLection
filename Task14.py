# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.
# 10 -> 1 2 4 8
n = 16
d = 0
t = 2
count = 0

while d < n:
    d = t**count
    count += 1
    if d <= n:
        print(d)

# i = 0
# while 2 ** i <= n:
#     print(2 ** i)
#     i += 1