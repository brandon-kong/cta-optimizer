"""
main.py
"""

from src.utils.data_loader import load_data
from src.utils.logger import Logger

def main():

    logger = Logger(log_file="logs/activity.log")
    logger.clear()

    train_system = load_data(
        base_path="./data",
        file_names=[
            "red_line.json"
        ])

    logger.log(f"Created TrainSystem with {len(train_system)} stations")

if __name__ == "__main__":
    main()