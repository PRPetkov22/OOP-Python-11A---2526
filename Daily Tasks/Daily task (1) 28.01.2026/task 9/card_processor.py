from payment_processor import PaymentProcessor


class CardProcessor(PaymentProcessor):
    def fee(self, amount):
        return amount * 0.025

    def pay(self, amount):
        fee_value = self.fee(amount)
        final_amount = amount + fee_value
        return final_amount, f"Paid by card. Fee: {fee_value:.2f}. Total: {final_amount:.2f}"