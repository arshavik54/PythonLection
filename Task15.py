# 15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя,
# а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей, а для 
# тещи полегче. Но вот незадача: арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему! Пользователь вводит одно
# число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой 
# строчке каждое. Здесь каждое число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

from random import randint


# count = int(input("Введите количество чисел: "))

# max_num = 0
# min_num = 1000

# for _ in range(count):
#     current_num = randint(1, 10)
#     print(current_num, end=" ")
#     if max_num < current_num: 
#         max_num = current_num
#     if min_num > current_num:
#         min_num = current_num
        

# print()
# print(min_num, max_num)

count = int(input("Введите количество чисел"))
current_num = randint(1, 10)
max_num = current_num
min_num = current_num

for _ in range(count - 1):
    current_num = randint(1, 10)
    print(current_num, end=" ")
    max_num = max(max_num, current_num)
    min_num = min(min_num, current_num)
        

print()
print(min_num, max_num)