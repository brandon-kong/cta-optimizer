import os
import unittest
from unittest.mock import patch, mock_open
from cta_optimizer.lib.logger import (
    Logger,
    LogLevel,
    format_log_message
)

LOG_FILE_PATH = "logs/test.log"
LOG_FILE_PATH_2 = "logs/test/test.log"


class TestLogger(unittest.TestCase):

    def tearDown(self):
        if os.path.exists(LOG_FILE_PATH):
            os.remove(LOG_FILE_PATH)

        if os.path.exists(LOG_FILE_PATH_2):
            os.remove(LOG_FILE_PATH_2)

        # remove the directory of log file path 2
        if os.path.exists("logs/test"):
            os.rmdir("logs/test")

    def test_logger_creates_object(self):
        logger = Logger(file_path=LOG_FILE_PATH, create_new_file=True)
        self.assertIsNotNone(logger)

    def test_logger_with_invalid_file_path(self):
        with self.assertRaises(ValueError):
            Logger(file_path=None)

        with self.assertRaises(ValueError):
            Logger(file_path=123)


    def test_logger_logs_info(self):
        logger = Logger(file_path=LOG_FILE_PATH, create_new_file=True)
        logger.info("Test info message")

        # Check if the log file was created and contains the message
        with open(LOG_FILE_PATH, "r", encoding="utf-8") as f:
            content = f.read()
            self.assertTrue("Test info message" in content)

    def test_logger_logs_error(self):
        logger = Logger(file_path=LOG_FILE_PATH, create_new_file=True)
        logger.error("Test error message")

        # Check if the log file was created and contains the message
        with open(LOG_FILE_PATH, "r", encoding="utf-8") as f:
            content = f.read()
            self.assertTrue("Test error message" in content)

    def test_logger_throw_error_on_invalid_message(self):
        logger = Logger(file_path=LOG_FILE_PATH, create_new_file=True)
        with self.assertRaises(ValueError):
            logger.info(None)

        with self.assertRaises(ValueError):
            logger.info(123)

        with self.assertRaises(ValueError):
            logger.info("")

    def test_format_log_message(self):
        message = format_log_message("Test message", LogLevel.INFO)
        self.assertTrue("INFO" in message)
        self.assertTrue("Test message" in message)

    def test_format_log_message_invalid_log_level(self):
        with self.assertRaises(ValueError):
            format_log_message("Test message", "INVALID")

    def test_format_log_message_invalid_message(self):
        with self.assertRaises(ValueError):
            format_log_message(None, LogLevel.INFO)

        with self.assertRaises(ValueError):
            format_log_message(123, LogLevel.INFO)

    def test_format_log_message_empty_message(self):
        with self.assertRaises(ValueError):
            format_log_message("", LogLevel.INFO)

    def test_delete_log_file_on_exit(self):
        logger = Logger(file_path=LOG_FILE_PATH, create_new_file=True, delete_file_on_exit=True)
        self.assertIsNotNone(logger)

        del logger

        # Check if the log file was deleted
        self.assertFalse(os.path.exists(LOG_FILE_PATH))

    def test_delete_log_file_on_exit_fails(self):
        logger = Logger(file_path=LOG_FILE_PATH, create_new_file=True, delete_file_on_exit=True)
        self.assertIsNotNone(logger)

        # Delete the log file before deleting the logger
        os.remove(LOG_FILE_PATH)

        del logger

        # Check if the log file was not deleted
        self.assertFalse(os.path.exists(LOG_FILE_PATH))

    @patch("builtins.open", side_effect=[OSError, mock_open()])
    def test_logger_creation_error_backup(self, mock_open):
        logger = Logger(file_path=LOG_FILE_PATH, create_new_file=True)
        self.assertTrue(logger.failed_to_open_file)
        self.assertTrue(logger.print_to_console)

    @patch("builtins.open", side_effect=OSError)
    def test_logger_creation_error_backup_with_no_created_file(self, mock_open):
        logger = Logger(file_path=LOG_FILE_PATH, create_new_file=True)
        self.assertTrue(logger.failed_to_open_file)
        self.assertTrue(logger.print_to_console)

    #@patch("builtins.open", side_effect=[mock_open(), mock_open()])
    def test_logger_creation_error_backup_succeeds(self):
        logger = Logger(file_path=LOG_FILE_PATH_2, create_new_file=True)
        self.assertFalse(logger.failed_to_open_file)

    @patch("builtins.open", side_effect=OSError)
    def test_logger_creation_error_backup_fails(self, mock_open):
        logger = Logger(file_path=LOG_FILE_PATH_2, create_new_file=False)
        self.assertTrue(logger.print_to_console)