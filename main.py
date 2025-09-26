from CsvReader import CsvReader
from CsvToJsonConverter import CsvToJsonConverter
from JsonReader import JsonReader
from StudentFinder import StudentFinder

if __name__ == "__main__":
    csv_url = "https://informer.com.ua/dut/python/import/st_gt.csv"
    csv_reader = CsvReader()
    data = csv_reader.read_data(csv_url)
    for row in data:
        print(row)

    json_path = "students_data.json"

    converter = CsvToJsonConverter()
    converter.read_and_convert(csv_url, json_path)

    json_reader = JsonReader()
    json_reader.display_data(json_path)

    finder = StudentFinder(json_reader)
    finder.load_data(json_path)
    print('Введіть прізвище студента: ')
    surname_to_find = input()
    found_students = finder.find_students_by_surname(surname_to_find)
    finder.display_students_info(found_students)