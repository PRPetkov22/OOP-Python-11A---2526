from data_exporter import DataExporter
import json

class JsonExporter(DataExporter):
    def export(self, rows):
        return json.dumps(rows, indent=2)