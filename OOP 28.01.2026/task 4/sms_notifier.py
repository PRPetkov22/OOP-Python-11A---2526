from notifier import Notifier

class SMSNotifier(Notifier):
    def send(self, to, message):
        return f"SMS sent to {to}: {message}"