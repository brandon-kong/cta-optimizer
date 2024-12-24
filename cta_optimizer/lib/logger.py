"""
logger.py
--------------
The Logger class is responsible for logging messages to a file and optionally to the console.
"""

import os
from datetime import datetime
from enum import StrEnum


class LogLevel(StrEnum):
    """
    Enum class for log levels
    """

    INFO = "INFO"
    ERROR = "ERROR"
    WARNING = "WARNING"


def format_log_message(message: str, level: LogLevel = LogLevel.INFO) -> str:
    """
    Format the log message with the current timestamp and log level

    :param message: The message to log
    :param level: The log level
    :return: The formatted log message
    """
    if not isinstance(level, LogLevel):
        raise ValueError("Invalid log level")

    if not isinstance(message, str):
        raise ValueError("Message must be a string")

    if len(message) == 0:
        raise ValueError("Message cannot be empty")

    return f"{datetime.now().isoformat()} {level}: {message}"


def validate_message(message: str):
    """
    Validate the message to ensure it is not empty or None

    :param message: The message to validate
    :return: True if the message is valid, False otherwise
    """
    if message is None:
        raise ValueError("Message cannot be None")

    if isinstance(message, str) is False:
        raise ValueError("Message must be a string")

    if len(message) == 0:
        raise ValueError("Message cannot be empty")


class Logger:

    def __init__(
        self,
        file_path: str = "logs/activity.log",
        print_to_console: bool = True,
        create_new_file: bool = False,
        delete_file_on_exit: bool = False,
    ):
        if file_path is None:
            raise ValueError("File path cannot be None")

        if not isinstance(file_path, str):
            raise ValueError("File path must be a valid string")
        # Initialize the logger with a file path

        self.print_to_console = print_to_console
        self.failed_to_open_file = False
        self.delete_file_on_exit = delete_file_on_exit

        if file_path:
            self.file_path = file_path

            try:
                with open(self.file_path, "a", encoding="utf-8") as f:
                    f.write("")
            except (OSError, TypeError):
                self.failed_to_open_file = True

                if create_new_file:
                    try:
                        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
                        # Create a new file if the file cannot be opened
                        with open(self.file_path, "w", encoding="utf-8") as cf:
                            cf.write("")

                        self.failed_to_open_file = False
                    except (OSError, TypeError):
                        self.print_to_console = True

                        print(
                            format_log_message(
                                f"Failed to open log file at {self.file_path}",
                                LogLevel.ERROR,
                            )
                        )
                else:
                    self.print_to_console = True

                # Default to printing to console if the file cannot be opened

    def info(self, message: str):
        self.__message(message, LogLevel.INFO)

    def error(self, message: str):
        self.__message(message, LogLevel.ERROR)

    def __message(self, message: str, level: LogLevel):
        validate_message(message)

        if self.print_to_console:
            print(format_log_message(message, level))

        if self.failed_to_open_file is False:
            with open(self.file_path, "a", encoding="utf-8") as f:
                f.write(format_log_message(message, level) + "\n")

    def __del__(self):
        if self.failed_to_open_file:
            return

        if self.delete_file_on_exit:
            try:
                os.remove(self.file_path)
            except OSError:
                pass


# Create pre-configured instances of the Logger class

default_logger = Logger(create_new_file=True)
