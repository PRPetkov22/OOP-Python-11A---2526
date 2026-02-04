from logger import Logger

class FileLogger(Logger):
    def log(self, message):
        return f"File log: {message}"