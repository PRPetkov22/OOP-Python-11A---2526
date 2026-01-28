from json_exporter import JsonExporter
from csv_exporter import CsvExporter

rows = [
    {"id": 1, "name": "Mancho", "age": 17},
    {"id": 2, "name": "Sachana", "age": 53}
]

json_exporter = JsonExporter()
csv_exporter = CsvExporter()

print(json_exporter.export(rows))
print()
print(csv_exporter.export(rows))