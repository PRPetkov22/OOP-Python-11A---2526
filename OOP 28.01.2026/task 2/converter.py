from abc import ABC, abstractmethod

class Converter(ABC):
    @abstractmethod
    def convert(self, value):
        pass