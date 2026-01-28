from card_processor import CardProcessor
from crypto_processor import CryptoProcessor

card = CardProcessor()
crypto = CryptoProcessor()

final1, msg1 = card.pay(280)
print(msg1)

final2, msg2 = crypto.pay(280)
print(msg2)