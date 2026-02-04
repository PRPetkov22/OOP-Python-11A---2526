from payment_method import PaymentMethod

class CashOnDelivery(PaymentMethod):
    def pay(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        return f"Paid {amount} cash on delivery"
