"""
train_station.py

This module contains the TrainStation class which is responsible for storing information
about a train station such as name, line, position, and transfer stations.
"""

from typing import List

from .position.position import Position
from .train_line import CTATrainLine

from src.utils.constants import FARE_COST


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

        self.transfer_stations: List[TrainTransfer] = []

    def add_transfer_station(self, station: "TrainTransfer") -> None:
        """
        Add a transfer station to the train station

        :param station: TrainStation
        """
        if station is None:
            raise ValueError("[TrainStation]: station is required")

        if not isinstance(station, TrainTransfer):
            raise ValueError(
                "[TrainStation]: station must be an instance of TrainTransfer"
            )

        self.transfer_stations.append(station)

    def get_transfer_stations(self) -> List["TrainTransfer"]:
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

    def get_id(self) -> str:
        """
        Get the unique identifier for the train station

        :return: str
        """
        return f"{self.line}:{self.name}"

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

    def __hash__(self):
        return hash((self.name, self.line, self.position))


class TrainAction:
    """
    TrainAction represents an action that can be taken at a train station
    """

    def __init__(self, source: TrainStation, cost: float = 0.0):
        self.__set_source(source)

        if not isinstance(cost, float):
            raise ValueError("[TrainAction]: cost must be a float")

        self.cost = cost

    def __set_source(self, source: TrainStation):
        if source is None:
            raise ValueError("[TrainAction]: source is required")
        if not isinstance(source, TrainStation):
            raise ValueError(
                "[TrainAction]: source must be an instance of TrainStation"
            )
        self.source = source

    def get_source(self) -> TrainStation:
        """
        Get the source train station

        :return: TrainStation
        """

        return self.source

    def get_cost(self) -> float:
        """
        Get the cost of the action

        :return: float
        """

        return self.cost

    def __str__(self):
        return f"Action[ {self.source} ]"


class TrainTransfer(TrainAction):
    """
    TrainTransfer represents a transfer between two train stations
    """

    def __init__(
        self, source: TrainStation, destination: TrainStation, is_paid: bool = False
    ):
        cost = is_paid and FARE_COST or 0.0

        super().__init__(source, cost=cost)
        self.__set_destination(destination)

    def __set_destination(self, destination: TrainStation):
        if destination is None:
            raise ValueError("[TrainTransfer]: destination is required")
        if not isinstance(destination, TrainStation):
            raise ValueError(
                "[TrainTransfer]: destination must be an instance of TrainStation"
            )
        self.destination = destination

    def get_source(self) -> TrainStation:
        """
        Get the source train station

        :return: TrainStation
        """

        return self.source

    def get_destination(self) -> TrainStation:
        """
        Get the destination train station

        :return: TrainStation
        """

        return self.destination

    def is_transfer_paid(self) -> bool:
        """
        Check if the transfer is paid

        :return: bool
        """

        return self.cost > 0.0

    def is_same_line(self) -> bool:
        """
        Check if the transfer is between stations on the same line

        :return: bool
        """

        return self.source.get_line() == self.destination.get_line()

    def __str__(self):
        return f"Transfer[ {self.source} -> {self.destination} ]"
