import os
from typing import TextIO


class HandBook:
    """
    Класс Телефонного справочника где хранятся записи 

    Args:
        *args : остальные позиционные аргументы
        **kwargs : остальные именованные аргументы

    Attributes:
        data_file_url (str) : сслыка на текстовый объект где хранятся записи
        records_num (int) : число записей в справочнике
    """
    def __init__(self, *args, **kwargs):
        self.data_file_url: str = 'data.txt'
        self.records_num : int = self.get_records_num()

    def get_records_num(self)-> int:
        """
        Метод Возвращает количество записей в справочнике

        Returns:
            records_num (int) : число записей в справочнике
        """
        with open(f'{self.data_file_url}', 'r') as data_file:
            records_num = len(data_file.readlines())
            return records_num

    def add_record(self, lastname: str, firstname: str, midllename: str,
                  company_name: str, work_phone_number: int, personal_phone_number: int) -> None:
        """
        Метод добавляет новую запись в справочник

        Params:
            lastname (str) : Фамилия человека
            firstname (str) : Имя человека
            midllename (str) : Отчество человека 
            company_name (str) : Название компании где человек работает
            work_phone_number (str) : Рабочий телефон компании
            personal_phone_number (str) : Сотовый телефон человека
        
        """
        with open(f'{self.data_file_url}', 'a') as data_file:
            self.records_num += 1
            data_file.write(f'{self.records_num} {lastname} {firstname} {midllename} {company_name} {work_phone_number} {personal_phone_number}\n')

    
    def page_records(self, start_index : int = 0) -> None :
        """
        Метод показвающий страницу справочника(в странице 5 записей) опираясь на айди записи

        Params:
            start_index (int) : Начальный индекс записи с помощью которого будут браться следующие 5 записей
            
        """
        data_file : TextIO = open(self.data_file_url, 'r')
        data : list = data_file.readlines()
        data_file.close()
        stop_index : int = start_index + 5
        if stop_index > len(data):
            stop_index = len(data)
        for i in range(start_index, stop_index):
            print(data[i],end='')





