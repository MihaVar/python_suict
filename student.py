from datetime import date

class Student:

    def __init__(self, surname: str, name: str, patronymic: str, group_number: str, birth_date: date):
        self.__surname = surname
        self.__name = name
        self.__patronymic = patronymic
        self.__group_number = group_number
        self.__birth_date = birth_date

    # Гетери
    def get_full_name(self) -> str:
        return f"{self.__surname} {self.__name} {self.__patronymic}"

    def get_surname(self) -> str:
        return self.__surname

    def get_name(self) -> str:
        return self.__name

    def get_patronymic(self) -> str:
        return self.__patronymic

    def get_group_number(self) -> str:
        return self.__group_number

    def get_birth_date(self) -> date:
        return self.__birth_date

    def set_group_number(self, new_group: str):
        self.__group_number = new_group

    def set_birth_date(self, new_date: date):
        self.__birth_date = new_date