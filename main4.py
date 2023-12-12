# def f(x):
#     return x*x
# print(f(5))

#___________________________________
# list_1 = [1,2,3,5,8,15,23,38]
# res = list()

# for i in list_1:
#     if i % 2 == 0:
#         res.append((i, i**2))

# print(res)

def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]
data = [1,2,3,5,8,15,23,38]
res = select(int,data)
res = where(lambda x: x % 2 == 0,res)