from email_notifier import EmailNotifier
from sms_notifier import SMSNotifier

email = EmailNotifier()
sms = SMSNotifier()

print(email.send("plamenraikovpetkov@abv.bg", "Hello with email"))
print(sms.send("088 554 6176", "Hello with SMS"))