import os
import unittest
from standalone.lib.logger import Logger


LOG_FILE_PATH = "logs/test.log"


class TestLogger(unittest.TestCase):

    def test_logger_creates_log_file(self):
        logger = Logger(file_path=LOG_FILE_PATH, create_new_file=True)
        self.assertIsNotNone(logger)

    def test_logger_does_not_create_log_file(self):
        logger = Logger(file_path='/path/that/does/not/exist/log.txt', create_new_file=False, print_to_console=False)

        # Check if the logger was created
        self.assertIsNotNone(logger)

        self.assertTrue(logger.is_print_to_console())

    def test_logger_creates_log_file_and_directories(self):
        # delete the log file if it exists
        if os.path.exists(LOG_FILE_PATH):
            os.remove(LOG_FILE_PATH)
            print(f"Deleted {LOG_FILE_PATH}")

        logger = Logger(file_path=LOG_FILE_PATH, create_new_file=True)
        self.assertIsNotNone(logger)

        # Check if the log file was created
        self.assertTrue(os.path.exists(LOG_FILE_PATH))

    def test_logger_does_not_create_log_file_and_directories(self):
        pass


    def test_logger_logs_info(self):
        logger = Logger(file_path=LOG_FILE_PATH, create_new_file=True)
        logger.info("Test info message")

        # Check if the log file was created and contains the message
        with open(LOG_FILE_PATH, "r", encoding="utf-8") as f:
            content = f.read()
            self.assertTrue("Test info message" in content)

    def test_logger_throw_error_on_invalid_message(self):
        logger = Logger(file_path=LOG_FILE_PATH, create_new_file=True)
        with self.assertRaises(ValueError):
            logger.info(None)

        with self.assertRaises(ValueError):
            logger.info(123)

        with self.assertRaises(ValueError):
            logger.info("")

    def test_logger_logs_error(self):
        logger = Logger(file_path=LOG_FILE_PATH, create_new_file=True)
        logger.error("Test error message")

        # Check if the log file was created and contains the message
        with open(LOG_FILE_PATH, "r", encoding="utf-8") as f:
            content = f.read()
            self.assertTrue("Test error message" in content)
