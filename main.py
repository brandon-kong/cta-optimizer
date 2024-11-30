"""
main.py
"""

from src.data_loader import load_data

def main():

    train_system = load_data(
        base_path="./data",
        file_names=[
            "red_line.json"
        ])

    print(f"Created TrainSystem with {len(train_system)} stations")

if __name__ == "__main__":
    main()