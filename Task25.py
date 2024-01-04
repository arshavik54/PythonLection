# Задача №25.  Напишите программу, которая принимает на вход строку,
# и отслеживает, сколько раз каждый символ уже встречался. Количество 
# повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

# text="a a a b c a a d c d d"
# list_symbols=text.split()
# print(list_symbols)
# uniq_symbols=dict()
# print(uniq_symbols)
# for symbol in list_symbols:
#     if symbol not in uniq_symbols:
#         uniq_symbols[symbol]=0
#         print(symbol, end=" ")
#     else:
#         uniq_symbols[symbol]+=1
#         print(f"{symbol}_{uniq_symbols[symbol]}", end=" ")
#     # print(uniq_symbols)
# 2
text="a a a b c a a d c d d"
list_symbols=text.split()
print(list_symbols)
uniq_symbols=dict()
print()
result=""
for symbol in list_symbols:
    if symbol not in uniq_symbols:
        result+=f"{symbol} "
    else:
        result+=f"{symbol}_{uniq_symbols[symbol]} "
    uniq_symbols[symbol]=uniq_symbols.get(symbol,0)+1
print(result.strip())
