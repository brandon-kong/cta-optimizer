"""
utils/logger.py

This module contains the Logger class which is responsible for logging messages to a file.
"""

import datetime

from enum import StrEnum


class LogScope(StrEnum):
    """
    The LogScope Enum is used to represent the different
    log scopes that can be used when logging a message.
    """

    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"


class Logger:
    """
    The Logger class is used to log messages to a file.
    """

    def __init__(self, log_file: str):
        if log_file is None:
            raise ValueError("[Logger]: log_file is required")

        if not isinstance(log_file, str):
            raise ValueError("[Logger]: log_file must be a string")

        self.log_file = log_file

    def log(self, message: str, scope: LogScope = LogScope.INFO) -> None:
        """
        Log a message to the log file

        :param message: str
        :param scope: LogScope
        """
        if scope is None:
            raise ValueError("[Logger]: scope is required")

        if message is None:
            raise ValueError("[Logger]: message is required")

        print(message)

        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(f"[{datetime.datetime.now()}] - {scope} - {message}\n")

    def clear(self) -> None:
        """
        Clear the log file

        :return: None
        """
        with open(self.log_file, "w", encoding="utf-8") as f:
            f.write("")
