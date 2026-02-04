from card_payment import CardPayment
from cash_on_delivery import CashOnDelivery

p1 = CardPayment("9191")
print(p1.pay(50))

p2 = CashOnDelivery()
print(p2.pay(20))
