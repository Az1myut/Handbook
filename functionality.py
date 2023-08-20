import time
from handbook import HandBook
from functools import reduce
def list_handbook_records(handbook: HandBook) -> None:
    """
    Функция для постраничного вывода записей из справочника

    Params:
    handbook (Handbook) : объект класса Справочника

    """

    # Если в справочнике 0 записей то мы возвращаем функцию 
    if handbook.records_num == 0:
        print('В справочнике нет записей')
        time.sleep(3)
        return 

    condition : bool = True
    print('В каждой странице содержится по 5 записей')
    time.sleep(3)
    start_index : int = 0
    # Выводим страницы записей пока они не закончатся или пока юзер не введет N
    while condition:
            handbook.page_records(start_index=start_index)
            start_index += 5
            # Проверка не закончились ли записи
            if start_index < handbook.records_num:
                not_correct_choice : bool = True
                while not_correct_choice:
                    print('Если хотите увидеть следущую страницу введите Y, в противном случае N')
                    choice : str = input('Ваш выбор: ')
                    if choice.upper() == 'Y':
                        break
                    elif choice.upper() == 'N':
                        return
                    else:
                        continue
            else:
                print()
                print('Больше не осталось записей')
                time.sleep(3)
                break

def add_record(handbook : HandBook) -> None:
    """
    Функция для добавления записи в справочник

    Params:
        handbook (Handbook) : объект класса Справочника
    """
    # Просим юзера вводить данные пока он не введет их правильно
    while True:
        lastname: str = input('Введите  фамилию: ')
        if lastname:
            break  
    while True:
        firstname: str = input('Введите  имя: ')
        if firstname:
            break  
    while True:
        midllename: str = input('Введите  отчество: ')
        if midllename:
            break  
    while True:
        company_name: str = input('Введите название компании: ')
        if company_name:
            break     
    while True:
        try:
            work_phone_number: int = int(input('Введите рабочий телефон: ')) 
            break
        except ValueError:
            print('Рабочий телефон должен содержать только цифры')
    while True:
        try:
            personal_phone_number: int = int(input('Введите сотовый телефон: '))
            break
        except ValueError:
            print('Сотовый телефон  должен содержать только цифры')
    # Вызываем метод Handbook(Справочника) для добавления записи
    handbook.add_record(lastname=lastname, firstname=firstname, midllename=midllename,
                        company_name=company_name, work_phone_number=work_phone_number,
                        personal_phone_number=personal_phone_number)    

def edit_record(handbook : HandBook):
    """
    Функция для редактирования записи в справочнике по айди записи

    Params:
        handbook (Handbook) : объект класса Справочника
    """
    print('Чтобы изменить запись вам нужно ввести айди записи')
    # Просим юзера ввести айди записи пока он не введет айди которое существует
    while True:
        try:
            pk : int = int(input('Айди записи: '))
            # Проверка на сущестовование айди
            if pk > handbook.records_num:
                print('Такой записи с таким айди не существует')
                # Спрашиваем юзера хочет ли он ввести другое айди или вернуться в главное меню
                while True:
                    print('Если хотите вернуться в меню то введите Y, если хотите ввести другое айди то введите N')
                    choice : str = input('Ваш выбор: ')
                    if choice.upper() == 'Y':
                        return
                    elif choice.upper() == 'N':
                        break
                    else:
                        continue
            else:
                break
        except ValueError:
            print('Айди является числом')
    # Открываем текстовый файл с данными чтобы загрузить данные в список
    with open(handbook.data_file_url, 'r') as data_file:
        data : list = data_file.readlines()
        edited_record : str = data[pk-1]
    # Находим запись которую юзер хотел редкатровать и выводим эту запись ему
    edited_record_chunks : list = edited_record.split(' ') 
    edited_record_chunks[-1] = edited_record_chunks[-1][:-1]
    edited_record_chunks.pop(0)
    edited_record = ' '.join(edited_record_chunks)
    print(edited_record)
    # Спрашиваем поочередно юзера хочет ли он оставить некоторые данные или хочет изменить
    for i in range(0,len(edited_record_chunks)):
        if i == 0:
            while True:
                print('Если хотите изменить фамилию то введите Y, в противном случае N')
                choice : str = input('Ваш выбор: ')
                if choice.upper() == 'Y':
                    while True:
                        lastname = input('Введите фамилию: ')
                        if lastname:
                            break
                    edited_record_chunks[i] = lastname
                    break
                elif choice.upper() == 'N':
                    break
                else:
                    continue
        elif i == 1:
            while True:
                print('Если хотите изменить имя то введите Y, в противном случае N')
                choice : str = input('Ваш выбор: ')
                if choice.upper() == 'Y':
                    while True:
                        firstname = input('Введите фамилию: ')
                        if firstname:
                            break
                    edited_record_chunks[i] = firstname
                    break
                elif choice.upper() == 'N':
                    break
                else:
                    continue
        elif i == 2:
            while True:
                print('Если хотите изменить отчество то введите Y, в противном случае N')
                choice : str = input('Ваш выбор: ')
                if choice.upper() == 'Y':
                    while True:
                        midllename = input('Введите отчество: ')
                        if midllename:
                            break
                    edited_record_chunks[i] = midllename
                    break
                elif choice.upper() == 'N':
                    break
                else:
                    continue
        elif i == 3:
            while True:
                print('Если хотите изменить название компании то введите Y, в противном случае N')
                choice : str = input('Ваш выбор: ')
                if choice.upper() == 'Y':
                    while True:
                        company_name = input('Введите название компании: ')
                        if company_name:
                            break
                    edited_record_chunks[i] = company_name
                    break
                elif choice.upper() == 'N':
                    break
                else:
                    continue
        elif i == 4:
            while True:
                print('Если хотите изменить рабочий телефон то введите Y, в противном случае N')
                choice : str = input('Ваш выбор: ')
                if choice.upper() == 'Y':
                    while True:
                        try:
                            work_phone_number = int(input('Введите рабочий телефон: '))
                            if work_phone_number:
                                break
                        except ValueError:
                            print('Рабочий телефон должен содержать только цифры')
                    edited_record_chunks[i] = str(work_phone_number)
                    break
                elif choice.upper() == 'N':
                    break
                else:
                    continue
        elif i==5:
            while True:
                print('Если хотите изменить сотовый телефон то введите Y, в противном случае N')
                choice : str = input('Ваш выбор: ')
                if choice.upper() == 'Y':
                    while True:
                        try:
                            personal_phone_number = int(input('Введите сотовый телефон: '))
                            if personal_phone_number:
                                break
                        except ValueError:
                            print('Сотовый телефон должен содержать только цифры')
                    edited_record_chunks[i] = str(personal_phone_number)
                    break
                elif choice.upper() == 'N':
                    break
                else:
                    continue
    # Заменяем старую запись на новую редактрованную
    edited_record_chunks.insert(0,f'{pk}')
    edited_record = ' '.join(edited_record_chunks)
    edited_record = edited_record + '\n'
    data[pk-1] = edited_record
    # Вписываем новые данные обратно в текстовый файл
    with open(handbook.data_file_url, 'w') as data_file:
        data_file.writelines(data)
    print(f'Вы успешно изменили запись номер {pk}')
    print(edited_record)
    time.sleep(3)
 
def check_choices(choices_list : list) ->bool:
    """
    Функция проверяет правильно ли ввел юзер варианты характеристики для поиска записей

    Params:
        choices_list (list) : Варианты характеристики для поиска записей
    
    Returns:
        False (bool) : Если варианты не прошли проверку
        new_choices_list (list) : Проверенные варианты характеристики для поиска записей
    """
    new_choices_list = []
    
    # Проверка на то что вариант характеристики является целым числом
    try:
        for choice  in choices_list:
            new_choices_list.append(int(choice))
    except ValueError:
        print('Ваш выбор должен состоять из чисел')
        time.sleep(3)
        return False
    # Проверка то что вариант характеристики находится в промежутку от 1 до 6 
    for i in choices_list:
        if int(i)>= 1 and int(i)<=6:
            pass
        else:
            print('Ваш выбор должен включать числа от 1 до 6')
            time.sleep(3)
            return False
    # Проверка то что юзер не ввел один и тот же вариант более одного раза
    if len(set(choices_list)) < len(choices_list):
        print('Нельзя вводить одно число больше одного раза')
        time.sleep(3)
        return False
    return new_choices_list

def search_word_in_records(handbook : HandBook, choice : int, word : str) -> list:
    """
    Функция для поска слова по данным записи

    Params:
        handbook (Handbook) : объект класса Справочника
        choice (int) : целое число соответсвующее виду данных записи
        word (str) : Слово введенное юзером
    Returns:
        found_records (set) : Записи в которых было найдено введенное слово
    """
    found_records = []
    # Открываем текстовый файл чтобы получить данные в виде списка
    with open(handbook.data_file_url, 'r') as data_file:
        data : list = data_file.readlines()
    # Проходимся по записям и проверяем находится ли введенное слово в определенном виде данных
    # Если находится то добавляем эту запись в список 
    for record in data:
        record_chunks = record.split(' ')
        if word.lower() in record_chunks[choice].lower():
            found_records.append(record)
    return set(found_records)


    

def search_records(handbook : HandBook):
    """
    Функция для Поиска записей по одной или нескольким характеристикам

    Params:
        handbook (Handbook) : объект класса Справочника
    """
    #Просим юзера ввести варианты характеристики для поиска записей пока он не введет их правильно
    while True:
        print('Чтобы сделать поиск записей в справочнике вам нужно выбрать характеристики поиска')
        print('Если хотите по сделать поиск по фамилии ВВЕДИТЕ 1')
        print('Если хотите по сделать поиск по имени ВВЕДИТЕ 2')
        print('Если хотите по сделать поиск по отчеству ВВЕДИТЕ 3')
        print('Если хотите по сделать поиск по названии компании ВВЕДИТЕ 4')
        print('Если хотите по сделать поиск по рабочему телефону ВВЕДИТЕ 5')
        print('Если хотите по сделать поиск по сотовому телефону ВВЕДИТЕ 6')
        print('Если хотите поиск по многим харкатеристикам то введите соответсвующие числа через пробел')
        choice : str = input('Ваш выбор: ')
        choices_list : list = choice.split(' ')
        # Вызываем функцию check_choices ради проверки валидности вариантов характеристики
        choices_list = check_choices(choices_list=choices_list) 
        # Если варианты характеристики валидные то пробегаемя по этим вариантам и спрашиваем юзера
        # ввести соответсвенно данные по этой характеристке
        if choices_list:
            all_founded_records = []
            for choice in choices_list:
                if choice == 1:
                    while True:
                        lastname = input('Введите фамилию: ')
                        if lastname:
                            break
                    # Вызываем функцию search_word_in_records чтобы узнать нашлось ли введеное слово в записях
                    # Если нашлось то мы добавляем эти записи в главный список найденных записей
                    found_records : list = search_word_in_records(handbook=handbook,choice=choice,word=lastname)
                    all_founded_records.append(found_records)
                elif choice == 2:
                    while True:
                        firstname = input('Введите имя: ')
                        if firstname:
                            break
                    # Вызываем функцию search_word_in_records чтобы узнать нашлось ли введеное слово в записях
                    # Если нашлось то мы добавляем эти записи в главный список найденных записей
                    found_records : list = search_word_in_records(handbook=handbook,choice=choice,word=firstname)
                    all_founded_records.append(found_records)
                elif choice == 3:
                    while True:
                        midllename = input('Введите отчество: ')
                        if midllename:
                            break
                    # Вызываем функцию search_word_in_records чтобы узнать нашлось ли введеное слово в записях
                    # Если нашлось то мы добавляем эти записи в главный список найденных записей
                    found_records : list = search_word_in_records(handbook=handbook,choice=choice,word=midllename)
                    all_founded_records.append(found_records)
                elif choice == 4:
                    while True:
                        company_name = input('Введите название компании: ')
                        if company_name:
                            break
                    # Вызываем функцию search_word_in_records чтобы узнать нашлось ли введеное слово в записях
                    # Если нашлось то мы добавляем эти записи в главный список найденных записей
                    found_records : list = search_word_in_records(handbook=handbook,choice=choice,word=company_name)
                    all_founded_records.append(found_records)
                elif choice == 5:
                    while True:
                        try:
                            work_phone_number: int = int(input('Введите рабочий телефон: ')) 
                            break
                        except ValueError:
                            print('Рабочий телефон должен содержать только цифры')
                    # Вызываем функцию search_word_in_records чтобы узнать нашлось ли введеное слово в записях
                    # Если нашлось то мы добавляем эти записи в главный список найденных записей
                    found_records : list = search_word_in_records(handbook=handbook,choice=choice,word=str(work_phone_number))
                    all_founded_records.append(found_records)
                elif choice == 6:
                    while True:
                        try:
                            personal_phone_number: int = int(input('Введите сотовый телефон: ')) 
                            break
                        except ValueError:
                            print('Сотовый телефон должен содержать только цифры')
                    # Вызываем функцию search_word_in_records чтобы узнать нашлось ли введеное слово в записях
                    # Если нашлось то мы добавляем эти записи в главный список найденных записей
                    found_records : list = search_word_in_records(handbook=handbook,choice=choice,word=str(personal_phone_number))
                    all_founded_records.append(found_records)
                
            # Вызываем функцию reduce из functools чтобы вывести только записи которые соответствуют всем характеристикам
            final_searched_records = reduce(lambda records1, records2: records1.intersection(records2),all_founded_records)
            # Если нашлись записи которые соответствуют всем характеристикам то мы выводим их в консоль
            if final_searched_records:
                for record in final_searched_records:
                    print(record,end='')
                time.sleep(3)
                break
            # Если  записи которые соответствуют всем характеристикам не нашлись  то мы выводим что не нашли никаих совпадений
            else:
                print('По вашему запросу не вышли результаты')
                time.sleep(3)
                break 
            
        else:
            continue






        
        
