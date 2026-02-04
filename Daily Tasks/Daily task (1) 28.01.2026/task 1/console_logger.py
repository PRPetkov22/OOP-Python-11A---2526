from logger import Logger

class ConsoleLogger(Logger):
    def log(self, message):
        print(f"Console log: {message}")