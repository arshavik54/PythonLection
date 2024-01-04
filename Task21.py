# Задача №21. 
# Напишите программу для печати всех уникальных значений в словарях.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально. Пользователь его не вводит

# Решение 1
list_dicts = [{"V": "S002"}, {"V": "S001", " VIII":" S007"}, {"VI": " S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "},
              {" VIII":" S007"}]

# unique_values = set()
#
# for cur_dict in list_dicts:
#     for key in cur_dict:
#         unique_values.add(cur_dict[key].strip())
#
# print(unique_values)

# Решение 2

# unique_values = set()
#
# for cur_dict in list_dicts:
#     for key in cur_dict.keys():
#         unique_values.add(cur_dict[key].strip())
#
# print(unique_values)

# Решение 3

# unique_values = set()
#
# for cur_dict in list_dicts:
#     for value in cur_dict.values():
#         unique_values.add(value.strip())
#
# print(unique_values)

# Решение 4

# unique_values = set()
#
# for cur_dict in list_dicts:
#     unique_values.add(*cur_dict.values())
#
# print(unique_values)

# Решение 5

unique_values = set()

for cur_dict in list_dicts:
    unique_values.update(cur_dict.values())

print(unique_values)