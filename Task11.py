# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6 
# Ряд чисел Фибоначчи:
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,
#233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, …

# n = int(input("Введите число больше 1:"))
# count = 4
# fib1 = 1
# fib2 = 1
# fib_res = fib1 + fib2

# while fib_res < n:    
#     fib1 = fib2
#     fib2 = fib_res
#     fib_res = fib2 + fib1
#     count += 1

# if fib_res == n:
#     print(count)
# else:
#     print(-1)

n = int(input("Введите число больше 1:"))



count = 4
fib2 = 1
fib_res = 2

while fib_res < n:
    fib2,fib_res = fib_res, fib2 + fib_res
    count += 1

if fib_res == n:
    print(count)
else:
    print(-1)