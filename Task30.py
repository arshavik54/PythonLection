# Заполните массив элементами арифметической прогрессии. Её первый элемент a1 , разность d 
# и количество элементов n будет задано автоматически. Формула для получения n-го члена 
# прогрессии: an = a1 + (n-1) * d.
# Пример
# На входе:

# a1 = 2
# d = 3
# n = 4
# На выходе:

# 2
# 5
# 8
# 11

a1 = 2
d = 3
n = 4
i = 0

# list_1 = []
# for i in range(n):
#     an = a1 + i * d
#     list_1.append(an)
# print(*list_1,sep = '\n')

for i in range(n):
  print(a1 + i * d)


                 