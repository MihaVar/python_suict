import json
from DataReader import DataReader

class JsonReader(DataReader):
    def read_data(self, path):
        with open(path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        return data

    def display_data(self, path):
        data = self.read_data(path)
        print("Дані прочитані з JSON файлу:")
        for row in data:
            print(row)