"""
train_station.py

This module contains the TrainStation class which is responsible for storing information
about a train station such as name, line, position, and transfer stations.
"""

from typing import List

from .position.position import Position
from .train_line import CTATrainLine


class TrainStation:
    """
    The TrainStation class is responsible for storing information about a train station
    such as name, line, position, and transfer stations.
    """

    def __init__(
        self, name: str = None, line: CTATrainLine = None, position: Position = None
    ):
        self.__set_name(name)
        self.__set_position(position)
        self.__set_line(line)

        self.is_open: bool = True

        self.transfer_stations: List[TrainStation] = []

    def add_transfer_station(self, station: "TrainStation") -> None:
        """
        Add a transfer station to the train station

        :param station: TrainStation
        """
        if station is None:
            raise ValueError("[TrainStation]: station is required")

        if not isinstance(station, TrainStation):
            raise ValueError(
                "[TrainStation]: station must be an instance of TrainStation"
            )

        self.transfer_stations.append(station)

    def get_transfer_stations(self) -> List["TrainStation"]:
        """
        Get all the transfer stations for the train station

        :return: List[TrainStation]
        """
        return self.transfer_stations

    def get_name(self) -> str:
        """
        Get the name of the train station

        :return: str
        """
        return self.name

    def get_position(self) -> Position:
        """
        Get the position of the train station

        :return: Position
        """
        return self.position

    def get_line(self) -> CTATrainLine:
        """
        Get the line of the train station

        :return: CTATrainLine
        """

        return self.line

    def close(self) -> None:
        """
        Closes the train station so that no trains can stop at the station

        :return: None
        """
        self.is_open = False

    def open(self) -> None:
        """
        Opens the train station so that trains can stop at the station

        :return: None
        """
        self.is_open = True

    def is_station_open(self) -> bool:
        """
        Check if the train station is open

        :return: bool
        """
        return self.is_open

    def __set_name(self, name: str):
        if name is None:
            raise ValueError("[TrainStation]: name is required")

        if not isinstance(name, str):
            raise ValueError("[TrainStation]: name must be a string")

        self.name = name

    def __set_position(self, position: Position):
        if position is None:
            raise ValueError("[TrainStation]: position is required")

        if not isinstance(position, Position):
            raise ValueError("[TrainStation]: position must be an instance of Position")

        self.position = position

    def __set_line(self, line: CTATrainLine):
        if line is not None and not isinstance(line, CTATrainLine):
            raise ValueError("[TrainStation]: line must be a string")

        self.line = line

    def __str__(self):
        return f"{self.name} ({self.line})"

    def __eq__(self, value: "TrainStation"):
        if value is None:
            return False

        if not isinstance(value, TrainStation):
            return False

        return (
            self.name == value.get_name()
            and self.line == value.get_line()
            and self.position == value.get_position()
        )
