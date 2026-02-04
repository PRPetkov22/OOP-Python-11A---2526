from payment_method import PaymentMethod

class CardPayment(PaymentMethod):
    def __init__(self, last4):
        self.last4 = str(last4)

    def pay(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        return f"Paid {amount} by card **** **** **** {self.last4}"
