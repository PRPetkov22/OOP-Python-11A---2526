from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass