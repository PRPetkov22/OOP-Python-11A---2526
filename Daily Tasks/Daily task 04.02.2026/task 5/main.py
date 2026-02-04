from email import Email
from sms import SMS
from push import Push

n = int(input())

for _ in range(n):
    data = input().split(maxsplit=1)
    notif_type = data[0]
    msg = data[1] if len(data) > 1 else ""

    if notif_type == "EMAIL":
        notification = Email()
    elif notif_type == "SMS":
        notification = SMS()
    elif notif_type == "PUSH":
        notification = Push()

    print(notification.send(msg))