# def sum_numbers(n):   def - функция
#     summa = 0
#     for i in range(1, n+1):
#         summa += i
#     return summa
#------------------------------------------------------------------------
# print(sum_numbers(5))
# def sum_str(*args):   # * можно передавать неограниченное кол-во элементов
#     res = ''
#     for i in args:
#         res += i
#     return res

# print(sum_str('q','e','l'))
# print(sum_str('q','e','l','hj','hj'))
# print(sum_str(1, 8, 7))
#---------------------------------------------------------------------------
# import modul as m                      # импортируем modul
# #from modul import max1     *         # напрямую modul     * если все функции

# print(m.max1(15,9))
#-----------------------------------------------------------------------
#Рекурсия Фибоначи

# def fib(n):
#     if n in [1,2]:
#         return 1
#     return fib(n-1) + fib(n-2)

# list_1 = []
# for i in range(1,10):
#     list_1.append(fib(i))
# print(list_1)
#-------------------------------------------

#Быстрая сортировка с помощью рекурсии
# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(greater)

# print(quick_sort([45,55,76,43,2,4,6,8,7,54]))  #[2, 4, 6, 7, 8, 43, 45, 54, 55, 76]
#--------------------------------------------------------------------------
#Сортировка слиянием

# def merge_sort(nums):
#     if len(nums) > 1:
#         mid = len(nums) // 2
#         left = nums[:mid]
#         right = nums[mid:]
#         merge_sort(left)
#         merge_sort(right)
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 nums[k] = left[i]
#                 i += 1
#             else:
#                 nums[k] = right[j]
#                 j += 1
#             k += 1

#         while i < len(left):
#             nums[k] = left[i]
#             i += 1
#             k += 1

# list1 = [434,5,5,776,6,4,69,7,6,542]
# merge_sort(list1)
# print(list1)