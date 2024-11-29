"""
position/position_factory.py

This module contains the PositionFactory class which is responsible for creating Position objects
and storing them in a dictionary to prevent creating duplicate Position objects.
"""

from typing import Dict

from .position import Position


class PositionFactory:
    """
    The PositionFactory class is responsible for creating Position objects
    and storing them in a dictionary to prevent creating duplicate Position objects.
    """

    positions: Dict[str, Position] = {}

    @staticmethod
    def get_position(latitude: float, longitude: float) -> Position:
        """
        Get a Position object based on the latitude and longitude

        :param latitude: float
        :param longitude: float
        :return: Position
        """

        formatted_position = Position.format_position(latitude, longitude)

        if formatted_position in PositionFactory.positions:
            return PositionFactory.positions[formatted_position]

        position = Position(latitude=latitude, longitude=longitude)
        PositionFactory.positions[formatted_position] = position

        return position

    @staticmethod
    def clear_positions() -> None:
        """
        Clear all the positions stored in the factory

        :return: None
        """
        PositionFactory.positions = {}

    def __len__(self) -> int:
        """
        Get the number of positions stored in the factory

        :return: int
        """
        return len(PositionFactory.positions.items())
