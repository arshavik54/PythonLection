# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 10). 
# В следующих строках располагается N целых чисел. Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

import random

n = int(input("Введите колличество дней от 1 до 10: "))
count = 0
max_count = 0

for i in range(n):

    temperature = random.randint(-50, 50)
    print(temperature, end = "  ")
    if temperature > 0:
        count += 1
        if max_count < count:
            max_count = count
    else:
        count = 0
print()
print(max_count)