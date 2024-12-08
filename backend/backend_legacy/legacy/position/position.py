"""
position/position.py

This module contains the Position class which is responsible for storing the latitude and longitude
of a position and calculating the distance between two positions.
"""

from typing import Dict


class Position:
    """
    The Position class is responsible for storing the latitude and longitude of a position
    and calculating the distance between two positions.
    """

    positions: Dict[str, "Position"] = {}

    def __init__(self, latitude: float = None, longitude: float = None):
        self.__set_latitude(latitude)
        self.__set_longitude(longitude)

    def __set_latitude(self, latitude: float):
        if latitude is None:
            raise ValueError("[Position]: latitude is required")

        if not isinstance(latitude, float):
            raise ValueError("[Position]: latitude must be a float")

        self.latitude = latitude

    def __set_longitude(self, longitude: float):
        if longitude is None:
            raise ValueError("[Position]: longitude is required")

        if not isinstance(longitude, float):
            raise ValueError("[Position]: longitude must be a float")

        self.longitude = longitude

    def get_latitude(self) -> float:
        """
        Get the latitude of the position

        :return: float
        """
        return self.latitude

    def get_longitude(self) -> float:
        """
        Get the longitude of the position
        """
        return self.longitude

    def distance_to(self, position: "Position") -> float:
        """
        Calculate the distance between two positions

        :param position: Position
        :return: float
        """
        if position is None:
            raise ValueError("[Position]: position is required")

        if not isinstance(position, Position):
            raise ValueError("[Position]: position must be an instance of Position")

        return (
            (self.latitude - position.get_latitude()) ** 2
            + (self.longitude - position.get_longitude()) ** 2
        ) ** 0.5

    @staticmethod
    def format_position(latitude: float, longitude: float) -> str:
        """
        Format the position as a string

        :param latitude: float
        :param longitude: float

        :return: str
        """
        return f"Position(latitude={latitude}, longitude={longitude})"

    def __str__(self) -> str:
        return Position.format_position(self.latitude, self.longitude)

    def __eq__(self, other: "Position") -> bool:
        if other is None:
            return False

        if not isinstance(other, Position):
            return False

        return (
            self.latitude == other.get_latitude()
            and self.longitude == other.get_longitude()
        )

    def __hash__(self):
        return hash((self.latitude, self.longitude))
