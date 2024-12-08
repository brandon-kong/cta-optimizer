import unittest
from standalone.lib.logger import Logger

LOG_FILE_PATH = "logs/test.log"


class TestLogger(unittest.TestCase):

    def test_logger_creates_log_file(self):
        logger = Logger(file_path=LOG_FILE_PATH, create_new_file=True)
        self.assertIsNotNone(logger)

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
