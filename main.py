from CsvReader import CsvReader
from CsvToJsonConverter import CsvToJsonConverter

if __name__ == "__main__":
    csv_url = "https://informer.com.ua/dut/python/import/st_gt.csv"
    csv_reader = CsvReader()
    data = csv_reader.read_data(csv_url)
    for row in data:
        print(row)

    json_path = "students_data.json"

    converter = CsvToJsonConverter()
    converter.read_and_convert(csv_url, json_path)