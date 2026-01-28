from data_exporter import DataExporter

class CsvExporter(DataExporter):
    def export(self, rows):
        if not rows:
            return ""

        headers = rows[0].keys()
        lines = []

        lines.append(",".join(headers))

        for row in rows:
            values = [str(row.get(h, "")) for h in headers]
            lines.append(",".join(values))

        return "\n".join(lines)