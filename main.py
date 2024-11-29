"""
main.py
"""

from src.train_line import CTATrainLine
from src.data_loader import DataLoader

def main():
    data_loader = DataLoader(base_path="./data")

    train_system = data_loader.load_data(
        [
            "red_line.json"
        ])

    print(f"Created TrainSystem with {len(train_system)} stations")

if __name__ == "__main__":
    main()