from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def act(self):
        pass

    @abstractmethod
    def react(self, event):
        pass

    @abstractmethod
    def interact(self, other):
        pass