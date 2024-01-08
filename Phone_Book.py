# Задача №55. Создать телефонный справочник с возможностью импорта и экспорта
# данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные,
# которые должны находиться в файле. 
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной
# записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

# Этапы работы:
# 1) Создать телефонный справочник:                      +
#     - Открыть файл в режиме добавления (a)             +
# 2) Добавить контакт:
#     - Запросить информацию у пользователя
#     - Подготовить данные в необходимом формате
#     - Открыть файл в режиме добавления (a)
#     - Добавить контакт в файл
# 3) Вывести данные из файла на экран:
#     - Открыть файл в режиме чтения (r)
#     - Вывести информацию на экран
# 4) Поиск данных:
#     - Запросить вариант поиска
#     - Запросить данные поиска
#     - Открыть файл в режиме чтения (r)
#     - Осуществить поиск по файлу
#     - Вывести нужную информацию на экран
# 5) Реализовать UI:
#     - Вывести варианты меню
#     - Получение запроса пользователя
#     - Реализация запроса пользователя
#     - Выход из программы
import shutil


def input_name():
    return input('Введите имя: ')

def input_surname():
    return input('Введите фамилию: ')

def input_patronymic():
    return input('Введите отчество: ')

def input_phone():
    return input('Введите номер телефона: ')

def input_address():
    return input('Введите адрес: ')

def create_contact():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    return f'{surname} {name} {patronymic} {phone}\n{address}\n\n'

def add_contact(contact):
    with open('phonebook.txt', 'a', encoding='UTF-8') as file:
        file.write(contact)

def copy_contact():
   
    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
        for nn, contact in enumerate(contacts_list, 1):
            print(nn,contact, '\n')
        num_copy = int(input('Выберите номер контакта, который хотите скопировать: '))
        index_contact = num_copy - 1
        
    with open('copy_phonebook.txt', 'a', encoding='UTF-8') as file:
        file.write(f'{contacts_list[index_contact]}\n\n')
    # with shutil.copy('phonebook.txt', 'r',encoding = 'UTF-8') as file:
    #      file.read(contacts_list)
    

def show_info():
    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
        for nn, contact in enumerate(contacts_list, 1):
            print(nn, contact)
        #print(file.read().rstrip())
        

def search_contact():
    print(
        'Возможные варианты поиска:\n'
        '1. По фамилии\n'
        '2. По имени\n'
        '3. По отчеству\n'
        '4. По номеру телефона\n'
        '5. По адресу\n'
    )
    var_search = input('Выберите вариант поиска: \n')

    while var_search not in ('1', '2', '3', '4', '5'):
        print('Некорректные данные, нужно ввести число комманды')
        var_search = input('Введите вариант поиска: ')

    index_var = int(var_search) - 1

    search = input('Введите данные для поиска: ')

    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')

    for contact_str in contacts_list:
        contact_lst = contact_str.replace('\n', ' ').split()
        if search in contact_lst[index_var]:
            print(contact_str)

def interface():
    with open('phonebook.txt', 'a', encoding='UTF-8'):
        pass
    command = '-1'
    while command != '5' and '2':
        print('Возможные варианты взаимодействия:\n'
              '1. Добавить контакт\n'
              '2. Скопировать контакт\n'
              '3. Вывести на экран\n'
              '4. Поиск контакта\n'
              '5. Выход из программы\n')

        command = input('Введите номер действия: ')

        while command not in ('1', '2', '3', '4', '5'):
            print('Некорректные данные, нужно ввести число комманды')
            command = input('Введите номер действия: ')

        match command:
            case '1':
                add_contact(create_contact())
            case '2':
                copy_contact()
            case '3':
                show_info()
            case '4':
                search_contact()
            case '5':
                print('Всего хорошего!')

interface()


# def show_info():
#     with open('phonebooke.txt', 'r', encoding='UTF-8') as file:
#         contacts_list = file.read().rstrip().split('\n\n')
#         #print(file.read().rstrip())
#         for contact in enumerate(contacts_list,1):
#             print(*contact)