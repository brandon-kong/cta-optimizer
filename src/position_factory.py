"""
position_factory.py

This module contains the PositionFactory class which is responsible for creating Position objects
and storing them in
"""


from typing import Dict

from .position import Position


class PositionFactory:

    positions: Dict[str, Position] = {}

    @staticmethod
    def create_position(latitude: float, longitude: float) -> Position:
        formatted_position = PositionFactory.format_position(latitude, longitude)

        if formatted_position in PositionFactory.positions:
            return PositionFactory.positions[formatted_position]
        
        position = Position(latitude=latitude, longitude=longitude)
        PositionFactory.positions[formatted_position] = position

        return position