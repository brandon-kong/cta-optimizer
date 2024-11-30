import datetime

from enum import StrEnum


class LogScope(StrEnum):
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"


class Logger:
    def __init__(self, log_file: str):
        if log_file is None:
            raise ValueError("[Logger]: log_file is required")

        if not isinstance(log_file, str):
            raise ValueError("[Logger]: log_file must be a string")

        self.log_file = log_file

    def log(self, message: str, scope: LogScope = LogScope.INFO) -> None:
        print(message)
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(f"[{datetime.datetime.now()}] - {scope} - {message}\n")
