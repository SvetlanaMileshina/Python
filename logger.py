from data_create import *

def create_contact():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    return f'{surname} {name} {patronymic}: {phone}\n{address}\n\n' 


def  add_contact():
    contact_str = create_contact()
    with open("phonebook.txt",'a',encoding='utf-8') as file: 
        file.write(contact_str) 

def print_contacts(): 
    with open("phonebook.txt",'r',encoding='utf-8') as file: 
        contacts_str = file.read()  
    contacts_list = contacts_str.rstrip().split('\n\n')
    for n,contact in enumerate(contacts_list, 1): # нумеруем список контактов начиная с 1,а не с 0.В n-номер контакта, в contact-сам контакт текущий, перебираем и 
        print(n,contact) # выводим на экран

def search_contact(): # функция поиск контакта пункт 4
    print ( # Выводим на экран возможные элементы поиска
            'Возможные варианты поиска: \n'
            '1 По фамилии\n'
            '2 По имени\n'
            '3 По отчеству \n'
            '4 По номеру телефона\n'
            '5 По адрессу(город)'
         ) 
        # создали переменную для запроса варианта поиска пункт 4
    var = input('Выберите вариант поиска:')#пользователь выбирает нужный вариант
    while var not in ('1','2','3','4','5'):# защита от некорректного ввода (not in - операторы вхождения и отрицания), не требует определения int, при такой записи кортежа пользователь вводит что угодно
        print('Некорректный ввод')
        var = input('Выберите вариант поиска')
    i_var = int(var) - 1 # преобразуем вариант пользователя в интовое значение и получаем Поиск по индексу  на единицу меньше
    
    search = input('Введите данные для поиска:').title()  #Получаем данные для поиска с большой буквы 
    with open("phonebook.txt",'r',encoding='utf-8') as file: # считываем файл
        contacts_str = file.read()   # сохраняем файл в строку
        contacts_list = contacts_str.rstrip().split('\n\n') # Преобразуем строку в список[](была строка с контактами, стал список с контактами),разделяем на контакты звпятыми с помощью функции split. Убираем ненужный пробел -функция strip, если rstrip- убираем пробелы только справа

    
    # Поиск данных в списке contact_list пункт 4
    for str_contact in contacts_list:# Перебираем контакты, преобразуем каждый контакт в список элементов контакта:строка фамилия, строка имя и т.д.
        lst_contact = str_contact.replace(':','').split()# В переменную lst_contact сохраняем данные контакта с заменой : и убираем \n\n
        if search in lst_contact[i_var]:# если  искомые данные есть в выбранном варианте lst-contact-список элементов контакта, то берем по индексу нужный элемент(фам илию,либо имя...) ['Иванов', 'Михаил', 'Петрович', '4953434596', 'Сочи']
            print(str_contact) # если совпадения есть, выводдим найденный контакт   

def copy_contact():
    with open("phonebook.txt",'r',encoding='utf-8') as file:
        contacts_str = file.read()
        contacts_list = contacts_str.rstrip().split('\n\n')
    for n,contact in enumerate(contacts_list, 1): # нумеруем список контактов начиная с 1,а не с 0.В n-номер контакта, в contact-сам контакт текущий, перебираем и 
        print(n,contact) # выводим на экран
    print()
    one_copy_cont = int(input('Выберите контакт по номеру для копирования'))
    print()
    # for n,contact in enumerate(contacts_list, 1): # нумеруем список контактов начиная с 1,а не с 0.В n-номер контакта, в contact-сам контакт текущий, перебираем и 
    #     if n == one_copy_cont:
    #         print(n,contact) 
    with open("phonebook1.txt",'a',encoding='utf-8')as file: 
        file.write(f'\n{contacts_list[one_copy_cont-1]}\n')