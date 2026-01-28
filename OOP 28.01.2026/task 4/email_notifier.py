from notifier import Notifier

class EmailNotifier(Notifier):
    def send(self, to, message):
        return f"Email sent to {to}: {message}"