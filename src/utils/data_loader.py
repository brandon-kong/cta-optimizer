"""
data_loader.py

This module contains the DataLoader class which is responsible for loading data from a JSON
file and converting it into a TrainSystem object.
"""

import json
from collections import deque
from typing import List

from ..train_line import CTATrainLine
from ..train_system import TrainSystem
from ..train_station import TrainStation, TrainTransfer

from ..position.position_factory import PositionFactory

from .is_rush_period import is_rush_period


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

    is_rush = is_rush_period()

    train_system = TrainSystem()

    # after all the stations are loaded, we will connect the transfer stations
    connection_queue = deque()

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

                    # Model the rush period
                    if "rush_period_only" in station and station["rush_period_only"]:
                        if not is_rush:
                            train_station.close()

                    # Add all transfer stations to the connection queue
                    if "transfers" in station:
                        for station_id, station_info in station["transfers"].items():
                            connection_queue.append(
                                (
                                    train_station,
                                    station_id,
                                    station_info.get("free", True),
                                )
                            )

                    # add the adjacent stations to the TrainStation
                    if "adjacent" in station:
                        for adjacent_station in station["adjacent"]:

                            connection_queue.append(
                                (train_station, adjacent_station, True)
                            )

                    # Add the station to the TrainSystem

                    train_system.add_station(train_station)

        except FileNotFoundError:
            print(f"File {file_name} not found")
            continue

    # Connect the transfer stations
    while connection_queue:
        station, station_id, fare = connection_queue.popleft()

        try:
            transfer_station = train_system.get_station_from_id(station_id)
        except ValueError as e:
            continue

        if transfer_station is None:
            print(f"Transfer station {station_id} not found")
            continue

        # create a transfer
        new_transfer = TrainTransfer(
            source=station, destination=transfer_station, is_paid=not fare
        )

        print(
            f"Adding transfer station {transfer_station.get_name()} to {station.get_name()}"
        )
        station.add_transfer_station(new_transfer)

    return train_system
