from abc import ABC, abstractmethod

class DataExporter(ABC):
    @abstractmethod
    def export(self, rows):
        pass