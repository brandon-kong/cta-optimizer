"""
data_loader.py

This module contains the DataLoader class which is responsible for loading data from a JSON
file and converting it into a TrainSystem object.
"""

import json
from typing import List

from .train_line import CTATrainLine
from .train_system import TrainSystem
from .train_station import TrainStation

from .position.position_factory import PositionFactory


def load_data(
    base_path: str = "./data", file_names: List[str] = None, line: CTATrainLine = None
) -> TrainSystem:
    """
    Load data from a JSON file and convert it into a TrainSystem object

    :param file_names: List[str]
    :return: TrainSystem
    """

    if file_names is None:
        raise ValueError("[DataLoader]: file_names is required")

    train_system = TrainSystem()

    for file_name in file_names:
        try:
            with open(f"{base_path}/{file_name}", "r", encoding="utf-8") as file:
                data = json.load(file)

                if "stations" not in data:
                    print(f"Stations not found in {file_name}")
                    continue

                stations = data["stations"]

                for station in stations:

                    if "name" not in station:
                        print(f"Name not found for station {station}")
                        continue

                    # create a Position object
                    if "position" not in station:
                        print(f"Position not found for station {station['name']}")
                        continue

                    if "lat" not in station["position"]:
                        print(f"Latitude not found for station {station['name']}")
                        continue

                    if "lng" not in station["position"]:
                        print(f"Longitude not found for station {station['name']}")
                        continue

                    position = PositionFactory.get_position(
                        latitude=station["position"]["lat"],
                        longitude=station["position"]["lng"],
                    )

                    # Get the line from the station data and create a CTATrainLine object

                    if line is None:
                        if "line" not in station:
                            print(f"Line not found for station {station['name']}")
                            continue

                        line = CTATrainLine(station["line"])

                    # create a TrainStation object

                    train_station = TrainStation(
                        name=station["name"],
                        line=line,
                        position=position,
                    )

                    if "closed" in station and station["closed"]:
                        train_station.close()

                    # Add the station to the TrainSystem

                    train_system.add_station(train_station)

        except FileNotFoundError:
            print(f"File {file_name} not found")
            continue

    return train_system
