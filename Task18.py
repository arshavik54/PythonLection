# Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k и вывести
# его. Считать, что такой элемент может быть только один. Если значение k совпадает с этим 
# элементом - выведите его.
# list_1 = [1, 2, 3, 4, 5, 5, 9, 7, 4, 2, 5, 7]
# k = 4
# # # 5

list_1 = [2, 4, 1, 6, 8, 2, 9, 3, 2, 5]
k = 9
razn = abs(list_1[0]-k)
req_elem = list_1[0]
for i in range(1,len(list_1)):
  if abs(list_1[i]-k)<razn:
    razn = abs(list_1[i]-k)
    req_elem = list_1[i]
print(req_elem)

# m = abs(k - list_1[0])  # модуль числа
# number = list_1[0]
# for i in range(1, len(list_1)):
#     if m > abs(list_1[i] - k):
#         m = abs(list_1[i] - k)
#         number = list_1[i]
# print(number)