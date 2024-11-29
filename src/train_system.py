"""
train_system.py

This module contains the TrainSystem class which is responsible for storing all the
train stations along with providing an API for filtering and searching for train stations based
on criteria such as line, position, and transfer stations.
"""

from typing import List, Dict, Set

from .train_station import TrainStation
from .train_line import CTATrainLine
from .position.position import Position

class TrainSystem:
    
    def __init__(self):
        self.stations: Dict[CTATrainLine, List[TrainStation]] = {}

    
    def add_station(self, station: TrainStation) -> None:
        if station is None:
            raise ValueError('[TrainSystem]: station is required')
        
        if not isinstance(station, TrainStation):
            raise ValueError('[TrainSystem]: station must be an instance of TrainStation')
        
        if station.get_line() not in self.stations:
            self.stations[station.get_line()] = []
        
        self.stations[station.get_line()].append(station)


    def get_stations_on_line(self, line: CTATrainLine) -> List[TrainStation]:
        if line not in self.stations:
            raise ValueError(f'[TrainSystem]: {line} line does not exist')
        
        return self.stations[line]
    

    def get_stations_near_position(self, position: Position, radius: float) -> Set[TrainStation]:
        stations_near_position = set()
        for _, stations in self.stations.items():
            for station in stations:
                if station.get_position().distance_to(position) <= radius:
                    stations_near_position.add(station)
        return stations_near_position
    

    def get_stations_with_transfer_stations(self) -> Set[TrainStation]:
        stations_with_transfer_stations = set()
        for _, stations in self.stations.items():
            for station in stations:
                if station.get_transfer_stations():
                    stations_with_transfer_stations.add(station)
        return stations_with_transfer_stations