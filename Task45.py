# Задача №45. Два различных натуральных числа n и m называются дружественными, если 
# сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот.
# Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары
# дружественных чисел, каждое из которых не превосходит k. Программа получает на
# вход одно натуральное число k, не превосходящее 105. Программа должна вывести все
# пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо
# выводить по одной в строке, разделяя пробелами. Каждая пара должна быть выведена
# только один раз (перестановка чисел новую пару не дает).
# Ввод:          Вывод:
# 300            220 284

def div_sum(number):
    sum_divs = 1
    for i in range(2, number):
        if number%i == 0:
            sum_divs += i
    return sum_divs


size = int(input('Введите предельное число К: '))

for num_1 in range(size):
    for num_2 in range(size):
        if div_sum(num_1) == num_2 and div_sum(num_2) == num_1 and num_1 < num_2:
            print(num_1, num_2)


# def div_sum(number):
#     sum_divs = 1
#     sq_num = number ** 0.5
#     if sq_num == int(sq_num):
#         sum_divs += sq_num
#     for div in range(2, int(number ** 0.5)):
#         if number % div == 0:
#             sum_divs += div + number // div
#     return sum_divs


# size = int(input('Введите предельное число К: '))

# for num_1 in range(2, size):
#     num_2 = div_sum(num_1)
#     if div_sum(num_2) == num_1 and num_1 < num_2:
#         print(num_1, num_2)

