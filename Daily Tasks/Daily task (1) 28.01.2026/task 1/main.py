from console_logger import ConsoleLogger
from file_logger import FileLogger

console_logger = ConsoleLogger()
console_logger.log("Hi console Plamen is here!")

file_logger = FileLogger()
result = file_logger.log("Hello file Plamen is here!")
print(result)