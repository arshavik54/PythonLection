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
#_______________________________________________


print(all([True, True, True, True]))
print(all([True, False, True, True]))
print(all([False, False, False, False]))
print()
print(any([True, True, True, True]))
print(any([True, False, True, True]))
print(any([False, False, False, False]))
print()
print(all([1, 2, 3, 4]))
print(all([1, 0, 3, 4]))
print(all([0, 0, 0, 0]))
print()
print(any([1, 2, 3, 4]))
print(any([1, 0, 3, 4]))
print(any([0, 0, 0, 0]))
print()
print(all(['dfg', 'sdf', 'sdf', 'cvb']))
print(all(['dfg', '', 'sdf', 'cvb']))
print(all(['', '', '', '']))
print()
print(any(['dfg', 'sdf', 'sdf', 'cvb']))
print(any(['dfg', '', 'sdf', 'cvb']))
print(any(['', '', '', '']))
print()
print(all([[''], ('',), {''}, ['']]))
print(all([[''], [], [''], ['']]))
print(all([{}, {}, {}, []]))
print()
print(any([[''], ('',), {''}, ['']]))
print(any([[''], [], [''], ['']]))
print(any([{}, {}, {}, []]))
print()
---------------------------------------------------------------

a = 'Python'
b = 'Hello world!'
z = 'Привет, меня зовут Вася!'

# print(a, b, z)
# print(a, b, z, sep=' ', end='\n')
# print(a, b, z, sep='-||-')
# print()
# print(a, end=z)
# print(b, end=z)
# print(z, end='\n')
=============================================

s = 'Python '

print(*s, sep=' ') # -> print('P', 'y', 't', 'h', 'o', 'n', ' ')
print()
print(*s, sep='\n')

# выведет:

# P y t h o n

# P
# y
# t
# h
# o
# n
-----------------------------------------------------------
name = "John"
print(f'Hi, {name}.') #- Hi, John.
print('Hi, %s.' % name) #- Hi, John
print('{} Hi, {}'.format(name[:2], name)) #- Hi, {name}
print('{b} Hi, {a}'.format(b=name[:2], a=name)) #- Hi, {name}
-------------------------------------------------------------------

import copy

my_list_1 = [123,234,3456,678,789, [111,222,[11,22,33],333,444]]
print(f'{my_list_1 =}')
my_list_2 = my_list_1
print(f'{my_list_2 =}')
print()
my_list_2[1] = 0
print(f'{my_list_1 =}')
print(f'{my_list_2 =}')
print()

my_list_3 = my_list_1.copy()
print(f'{my_list_1 =}')
print(f'{my_list_3 =}')
print()
my_list_3[2] = 999999
print(f'{my_list_1 =}')
print(f'{my_list_3 =}')
my_list_3[-1][2][1] = 'XXXX'
print(f'{my_list_1 =}')
print(f'{my_list_3 =}')

my_list_4 = my_list_1[:]

my_list_5 = copy.deepcopy(my_list_1)
print(f'{my_list_1 =}')
print(f'{my_list_5 =}')
print()
my_list_5[2] = 777777
print(f'{my_list_1 =}')
print(f'{my_list_5 =}')
my_list_5[-1][2][1] = '~~~~~~'
print(f'{my_list_1 =}')
print(f'{my_list_5 =}')
============================================================

q,*w, e = (11, 22, 33, 44, 55)
print(q)
print(w)
print(e)

q,*w, e = (11, 22, 33)
print(q)
print(w)
print(e)

q,*w, e = (11, 22)
print(q)
print(w)
print(e)
-------------------------------------------------------------------

my_list = [(1,2,3,4,5), (11,22,33), (111,222)]
for q,w,*e in my_list:
print(q,w,e, sep=' -\\- ')