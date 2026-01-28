from parser import Parser

class KeyValueParser(Parser):
    def parse(self, text):
        result = {}

        pairs = text.split(";")
        for pair in pairs:
            key, value = pair.split("=")
            result[key] = value

        return result