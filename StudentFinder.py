class StudentFinder:
    def __init__(self, json_reader):
        self.json_reader = json_reader
        self.data = None

    def load_data(self, path):
        self.data = self.json_reader.read_data(path)

    def find_students_by_surname(self, surname):
        if not self.data:
            raise ValueError("Дані не завантажено")
        return [student for student in self.data if student['Прізвище'] == surname]
