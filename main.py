from datetime import date

import student
import operations
import performance

if __name__ == "__main__":
    student = student.Student(
        surname="Маляр",
        name="Роман",
        patronymic="Олексійович",
        group_number="ПДМ-51",
        birth_date=date(2004, 4, 9)
    )

    subjects = ["DevOps", "ІППЗ", "МПНД"]
    real_scores = [80, 85, 75]
    desired_scores = [90, 90, 90]
    desired_avg = 90.0

    real_performance = performance.RealPerformance(subjects, real_scores)
    desired_performance = performance.DesiredPerformance(subjects, desired_scores, desired_avg)

    real_avg = real_performance.calculate_average_score()
    print(f"Розрахований реальний середній бал: {real_avg:.2f}")
    print(f"Бажаний середній бал: {desired_performance.calculate_average_score():.2f}")

    student_data_aggregator = operations.StudentData(student, real_performance, desired_performance)
    data_dictionary = student_data_aggregator.get_data_dict()
    print("Структура даних (Словник):")
    work_number = 1

    json_saver = operations.JSONSaver(student_data_aggregator, work_number)
    json_saver.save()

    csv_saver = operations.CSVSaver(student_data_aggregator, work_number)
    csv_saver.save()