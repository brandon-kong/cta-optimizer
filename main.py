"""
main.py
"""

from src.utils.data_loader import load_data
from src.utils.logger import default_logger

def main():

    default_logger.clear()

    train_system, train_graph = load_data(
        base_path="./data",
        file_names=[
            "red_line.json",
            "yellow_line.json",
        ])
    
    station_1 = train_system.get_station_from_id("red:Howard")
    station_2 = train_system.get_station_from_id("red:Loyola")

    shortest_path = train_graph.get_shortest_path(station_1, station_2)

    for station in shortest_path:
        print(station)

if __name__ == "__main__":
    main()