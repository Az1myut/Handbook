from handbook import HandBook
import time

from functionality import(
    list_handbook_records,
    add_record,
    edit_record,
    search_records
)


def main():
    """
    Главная функция для взаимодействия со справочником

    """
    handbook : HandBook = HandBook()
    condition : bool = True
    print('Давайте начнем взаимодействовать с нашим телефонным справочником')
    # Просим юзера вводить валидные варианты пока он их не введет
    while condition:
        print('Чтобы вывести постранично записи из справочника на экран, то ВВЕДИТЕ 1')
        print('Чтобы добавить новую запись в справочник, то ВВЕДИТЕ 2')
        print('Чтобы редактировать записи из справочника, то ВВЕДИТЕ 3')
        print('Чтобы сделать поиск записей по одной или нескольким характеристикам, то ВВЕДИТЕ 4')
        print('Чтобы прекратить взаимодействовать с нашим телефонным справочником, то ВВЕДИТЕ 5')
        # Проверка то что вариант является целым числом
        try:
            choice : int = int(input('Ваш выбор: '))
        except ValueError:
            print('Можно вводить только число')
            time.sleep(3)
            continue
        # Если вариант равен 1  то вызываем функцию вывода постранично записей из справочника на экран
        if choice == 1:
            list_handbook_records(handbook = handbook)
        # Если вариант равен 2  то вызываем функцию добавления новой записи в справочник
        elif choice == 2:
            add_record(handbook = handbook)
            print('Вы успешно добавили запись')
            time.sleep(3)
        # Если вариант равен 3  то вызываем функцию редактирования записей в справочнике
        elif choice == 3:
            edit_record(handbook=handbook)
        # Если вариант равен 4  то вызываем функцию поиска записей по одной или нескольким характеристикам
        elif choice == 4:
            search_records(handbook=handbook)
        # Если вариант равен 5  то завершаем программу
        elif choice == 5:
            return
        else:
            print('Вы ввели не правильное число')
            time.sleep(3)
            continue

main()