import json
from CsvReader import CsvReader

class CsvToJsonConverter(CsvReader):
    def convert_to_json(self, path, json_path):
        data = self.read_data(path)
        with open(json_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)

    def read_and_convert(self, csv_url, json_path):
        self.convert_to_json(csv_url, json_path)
        print(f"Дані з CSV було успішно конвертовано у JSON і збережено у файлі {json_path}.")