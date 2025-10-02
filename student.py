from datetime import date
import performance


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


class StudentData:
    def __init__(self, student: Student, real_performance: performance.RealPerformance, desired_performance: performance.DesiredPerformance):
        self.__student = student
        self.__real_performance = real_performance
        self.__desired_performance = desired_performance

    def get_data_dict(self) -> dict:
        real_subjects = self.__real_performance.get_subjects()
        desired_subjects = self.__desired_performance.get_subjects()

        if real_subjects != desired_subjects:
            raise ValueError("Списки предметів у реальній та бажаній успішності повинні збігатися!")

        real_scores = self.__real_performance.get_scores()
        desired_scores = self.__desired_performance.get_desired_scores()

        academic_details = []
        for subject, real_score, desired_score in zip(real_subjects, real_scores, desired_scores):
            academic_details.append({
                "Предмет": subject,
                "Реальний_Бал": real_score,
                "Бажаний_Бал": desired_score
            })

        data = {
            "Студент": {
                "ПІБ": self.__student.get_full_name(),
                "Номер_Групи": self.__student.get_group_number(),
                "Дата_Народження": self.__student.get_birth_date().isoformat(),
            },
            "Успішність": {
                "Деталі_успішності": academic_details,
                "Реальний_Середній_Бал": self.__real_performance.calculate_average_score(),
                "Бажаний_Середній_Бал": self.__desired_performance.calculate_average_score(),
            }
        }
        return data

    def get_filename_base(self) -> str:
        surname = self.__student.get_surname()
        group = self.__student.get_group_number()
        return f"{surname}_{group}"