from abc import ABC, abstractmethod

class Cache(ABC):
    @abstractmethod
    def set(self, key, value, ttl=None):
        pass

    @abstractmethod
    def get(self, key):
        pass