from card import Card
from cash import Cash
from crypto import Crypto

n = int(input())

for _ in range(n):
    data = input().split()
    method = data[0]
    amount = data[1]

    if method == "CARD":
        payment = Card()
    elif method == "CASH":
        payment = Cash()
    elif method == "CRYPTO":
        payment = Crypto()

    print(payment.pay(amount))