#list_1 = [12, 7, -1, 24, 0]
#print(list_1)
#list_1 = list()
#list_1 = [1, 2, 5, 8]
#print(*list_1)        # * без скобок и всякой ерунды
#for i in list_1:
#    print(i)
#print(len(list_1))  #len - выводит в консоль кол-во элементов
#print(list_1[-2])    # [3]- 'индекс элемента. [-1] - индекс с конца
#---------------------------------------------------------------------------
# print (list_1)
# list_1.append(8)            # .append добаыляет новый элемент в список
# print(list_1)
#----------------------------------------------------------------------------
# for i in range(5):
#     list_1.append(i)    # выводит поочередно добавленый символ
#     print(list_1)
#----------------------------------------------------------------------------
#Удаление последнего элемента списка
# print(list_1.pop())   # ВЫводит число, котрое удаляет
# print(list_1)         # выводит с уже удаленным символом
# print(list_1.pop())
# print(list_1)
# print(list_1.pop())
# print(list_1)
#--------------------------------------------------------------------------------
#Удаление конкретного элемента
# print(list_1.pop(0))    #Удалил элемент под  i = 0
# print(list_1)
#---------------------------------------------------------------------------------

# ДОБАВЛЕНИЕ ЭЛЕМЕНТА НА НУЖНУЮ ПОЗИЦИЮ

# print(list_1)
# print(list_1.insert(2,11))    # добавил во 2 эл 11
# print(list_1)
#--------------------------------------------------------------

#СРЕЗЫ

#list_1 = [1,2,3,4,5,6,7,8,9,10]
# print(list_1[0])              #1
# print(list_1[1])              #2
# print(list_1[-1])  #10
# print(list_1[-5])  #6
# print(list_1[:])   #[1,2,3,4,5,6,7,8,9,10]
# print(list_1[:2])  #[1,2]
# print(list_1[len(list_1)-2:])  #[9,10]
# print(list_1[2:9]) # [3,4,5,6,7,8,9]   последний не берем
#print(list_1[6:-18]) # []
# print(list_1[0:len(list_1):6])  #[1,7]
# print(list_1[::6])   #[1,7]
#-------------------------------------------------------------
#КОРТЕЖИ
# t = ()

# print(type(t))   #тип

# t = (1,5,3,)
# print(type(t))

# v = [1,8,9]
# print(v)
# print(type(v))

# v = tuple(v)    #кортеж
# print(v)
# print(type(v))

# a,b,c = v
# print(a,b,c)
#-----------------------------------------------------------
#Словари
# d={}
# d = dict()

# d['q']='qwerty'
# print(d)

# d['w'] = 'werty'
# print(d['q'])
#---------------------------------
# Множества
# colors = {'red', 'green', 'blue'}  # множества
# print(colors) #{'red',green', 'blue'} 
# colors.add('red')
# print(colors) # {'red',green', 'blue'} 
# colors.add('gray')
# print(colors)   # {'red',green', 'blue', gray} 
# colors.remove('red')
# print(colors)   # {green', 'blue', gray} 
# #colors.remove('red')  # KeyError: 'red'
# colors.discard('red') # ok
# print(colors) #  {green', 'blue', gray} 
# colors.clear()  # { }
# print(colors) # set()

# Операции со иножествами

# a = {1,2,3,5,8}
# b = {2,5,8,13,21}
# c = a.copy()    #c = {1,2,3,5,8}
# u = a.union(b)  # u = {1,2,3,5,8,13,21}
# i = a.intersection(b)  # i = {8,2,5}
# d1 = a.difference(b) #d1 = {1,3}
# dr = b.difference(a)  # dr = {13,21}
# q = a.union(b).difference(a.intersection(b)) # {1,21,3,13}
#_________________________________________________________

#Задача. создать список чисел от 1 до 100
#list_1 = []
# for i in range(1,101):
#     list_1.append(i)
# list_1 = [i for i in range(1, 101)]
# print(list_1)

#Задача. добавить только четные числа.
# list_1 = [i for i in range(1, 101) if i % 2 == 0]
# print(list_1)

#list_1 = [i * 2 for i in range(10) if i % 2 ==0]
#print(list_1)