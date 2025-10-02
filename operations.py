import json
from abc import ABC, abstractmethod

import performance
from student import Student


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

class DataSaver(ABC):
    def __init__(self, student_data: StudentData, work_number: int):
        self._data = student_data.get_data_dict() # Словник з даними
        self._filename_base = student_data.get_filename_base()
        self._work_number = work_number

    @abstractmethod
    def save(self):
        pass

    def _get_full_filename(self, format_extension: str) -> str:
        return f"{self._filename_base}_{self._work_number}.{format_extension}"

class JSONSaver(DataSaver):
    def save(self):
        filename = self._get_full_filename("json")
        with open(filename, 'w', encoding='utf-8') as f:
            # Використовуємо ensure_ascii=False для коректного збереження кирилиці
            json.dump(self._data, f, ensure_ascii=False, indent=4)
        print(f"✅ Дані успішно збережено у JSON файл: {filename}")