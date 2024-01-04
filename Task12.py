# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
s = 4 
p = 4

# sum = 0
# if 10 < s < 99:
#     while s > 0:
#         a = s % 10
#         sum = sum + a
#         s = s // 10
# else: sum = s // 2

# mult = p // sum
# print(sum, mult)

solutions = []
for i in range(1, 1001):
    for j in range(1, 1001):
        if s == i + j and p == i * j:
            solutions.append((min(i, j), max(i, j)))
solutions = list(set(solutions))

for solution in solutions:
    print(solution[0], solution[1])
