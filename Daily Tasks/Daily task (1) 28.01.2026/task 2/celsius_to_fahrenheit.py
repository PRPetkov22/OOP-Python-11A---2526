from converter import Converter

class CelsiusToFahrenheit(Converter):
    def convert(self, value):
        return (value * 9 / 5) + 32