from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def work(self):
        pass
