# Задача 26: Напишите программу, которая на вход принимает два числа A и B, и 
# возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8
a = int(input("Enter digit a: "))
b = int(input("Enter digit b: "))
# def f(a, b):
#     if b ==0:
#         return 1
#     return a**b
# print(f(a, b))
# ========================================
def f(a, b):
  if b == 0:
    return 1
  return f(a, b - 1) * a
print(f(a, b))