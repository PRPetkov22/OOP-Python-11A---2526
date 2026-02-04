from payment_processor import PaymentProcessor


class CryptoProcessor(PaymentProcessor):
    def fee(self, amount):
        return (amount * 0.01) + 0.50

    def pay(self, amount):
        fee_value = self.fee(amount)
        final_amount = amount + fee_value
        return final_amount, f"Paid by crypto. Fee: {fee_value:.2f}. Total: {final_amount:.2f}"