"""
station_data_loader.py

The DataLoader class is responsible for loading station
data from a file and returning a list of Station objects.
"""

import json
from typing import List, Optional
from pydantic import BaseModel, ValidationError

from cta_optimizer.location import Location
from cta_optimizer.station import Station


class TransferData(BaseModel):
    free_transfer: Optional[bool]


class Position(BaseModel):
    lat: float
    lng: float


class StationStop(BaseModel):
    name: str
    route: str
    position: Position
    adjacent_stations: List[str]
    transfer_stations: dict[str, TransferData]


class StationData(BaseModel):
    route_name: str
    speed: float
    stations: List[StationStop]


class StationDataLoader:
    def __init__(self, files: List[str] = None):
        if files is None:
            raise ValueError("Filename cannot be None")

        if not isinstance(files, list):
            raise ValueError("Filename must be a string")

        if len(files) == 0:
            raise ValueError("Filename cannot be empty")

        self.files = files

    def load_stations(self) -> List[Station]:
        """
        Load station data from the specified file and return a list of Station objects

        :param filename: The name of the file to load
        :return: A list of Station objects
        """

        # Load the station data from the JSON file
        try:
            stations = {}
            station_data = []

            for file in self.files:
                with open(file, "r") as file:
                    data = json.load(file)

                    this_station_data = StationData(**data)
                    station_data.append(this_station_data)

                    # create all the stations before adding adjacent stations
                    for station in this_station_data.stations:
                        station_id = f"{station.route}:{station.name}"
                        stations[station_id] = Station(station.name, Location(station.position.lat, station.position.lng))

            for station_data_file in station_data:
                # add adjacent stations
                for station in station_data_file.stations:
                    station_id = f"{station.route}:{station.name}"
                    for adjacent_station_id in station.adjacent_stations:

                        if adjacent_station_id not in stations:
                            continue

                        adjacent_station = stations[adjacent_station_id]
                        stations[station_id].add_adjacent_station(adjacent_station)

            return list(stations.values())

        except (OSError, json.JSONDecodeError) as e:
            print(f"Error loading station data: {e}")
            return []
        except ValidationError as e:
            print(f"Error validating station data: {e}")
            return []
