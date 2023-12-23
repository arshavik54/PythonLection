my_list = [1,2,34,5,7,8,90,0,3,67,89,35,2]


res_list = list(filter(lambda x: x % 2 == 0, my_list))
print(res_list)

# for el in res_list:
#     print(el, end=' ')
# print()

res_list=[]
f = lambda x: x % 2 == 0
for el in my_list:
    if f(el):
        res_list.append(el)
print(res_list)

# ----------------------------------------------------------

res_list = list(map(lambda x: x ** 2 , my_list))
print(res_list)

res_list=[]
f = lambda x: x ** 2
for el in my_list:
    res_list.append(f(el))
print(res_list)
# _____________________________________________________
my_list = [1,2,34,5,7,8,90,0,3,67,89,35,2]

numbers = input('Введите цифры через пробел').split()
print(numbers)
res_list = list(map(int , numbers))
print(res_list)
print([int(el) for el in numbers])