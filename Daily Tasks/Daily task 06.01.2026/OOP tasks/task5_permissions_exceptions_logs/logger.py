from datetime import datetime

class Logger:
    def __init__(self):
        self.logs = []

    def log(self, message):
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.logs.append(f"[{time_now}] {message}")

    def show_logs(self):
        for log in self.logs:
            print(log)