from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def fee(self, amount):
        pass

    @abstractmethod
    def pay(self, amount):
        pass