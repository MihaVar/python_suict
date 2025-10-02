import csv
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
        self._data = student_data.get_data_dict()
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
            json.dump(self._data, f, ensure_ascii=False, indent=4)
        print(f"Дані успішно збережено у JSON файл: {filename}")


class CSVSaver(DataSaver):
    def save(self):
        filename = self._get_full_filename("csv")
        student_info = self._data["Студент"]
        performance_info = self._data["Успішність"]
        fieldnames = ["ПІБ", "Номер_Групи", "Дата_Народження", "Реальний_Середній_Бал", "Бажаний_Середній_Бал"]

        row = {
            "ПІБ": student_info["ПІБ"],
            "Номер_Групи": student_info["Номер_Групи"],
            "Дата_Народження": student_info["Дата_Народження"],
            "Реальний_Середній_Бал": performance_info["Реальний_Середній_Бал"],
            "Бажаний_Середній_Бал": performance_info["Бажаний_Середній_Бал"],
        }

        for item in performance_info["Деталі_успішності"]:
            subject = item["Предмет"]
            real_key = f"{subject}_Реальний_Бал"
            desired_key = f"{subject}_Бажаний_Бал"

            fieldnames.extend([real_key, desired_key])
            row[real_key] = item["Реальний_Бал"]
            row[desired_key] = item["Бажаний_Бал"]

        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()
            writer.writerow(row)

        print(f"Дані успішно збережено у CSV файл: {filename}")