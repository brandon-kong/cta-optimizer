"""
train_system.py

This module contains the TrainSystem class which is responsible for storing all the
train stations along with providing an API for filtering and searching for train stations based
on criteria such as line, position, and transfer stations.
"""

from typing import List, Dict

from .train_station import TrainStation
from .train_line import CTATrainLine


class TrainSystem:
    """
    The TrainSystem class is responsible for storing all the train stations along
    with providing an API for filtering and searching for train stations based on
    criteria such as line, position, and transfer stations.
    """

    def __init__(self):
        self.stations: Dict[CTATrainLine, List[TrainStation]] = {}

    def add_station(self, station: TrainStation) -> None:
        """
        Add a station to the TrainSystem

        :param station: TrainStation
        :return: None
        """

        if station is None:
            raise ValueError("[TrainSystem]: station is required")

        if not isinstance(station, TrainStation):
            raise ValueError(
                "[TrainSystem]: station must be an instance of TrainStation"
            )

        if station.get_line() not in self.stations:
            self.stations[station.get_line()] = []

        self.stations[station.get_line()].append(station)

    def get_stations_on_line(self, line: CTATrainLine) -> List[TrainStation]:
        """
        Get all the stations on a specific line

        :param line: CTATrainLine
        :return: List[TrainStation]
        """
        if line not in self.stations:
            raise ValueError(f"[TrainSystem]: {line} line does not exist")

        return self.stations[line]

    def get_station_from_id(self, station_id: str = None) -> TrainStation:
        """
        Get a station based on the station id

        The station ID is formatted as follows: {line}:{name}

        :param station_id: str
        :return: TrainStation
        """
        if station_id is None:
            raise ValueError("[TrainSystem]: station_id is required")

        line, name = station_id.split(":")

        if line not in self.stations:
            raise ValueError(f"[TrainSystem]: {line} line does not exist")

        for station in self.stations[line]:
            if station.get_name() == name and station.get_line() == line:
                return station

        return None

    def __len__(self):
        count = 0

        for _, stations in self.stations.items():
            count += len(stations)

        return count
