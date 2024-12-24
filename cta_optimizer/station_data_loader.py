"""
station_data_loader.py

The DataLoader class is responsible for loading station
data from a file and returning a list of Station objects.
"""

import json
from typing import List, Optional
from pydantic import BaseModel, ValidationError

from cta_optimizer.models.location import Location
from cta_optimizer.models.station import Station


class TransferData(BaseModel):
    free_transfer: Optional[bool]


class AdjacentData(BaseModel):
    pass


class Position(BaseModel):
    lat: float
    lng: float


class StationStop(BaseModel):
    name: str
    closed: bool = False
    route: str
    position: Position
    adjacent_stations: List[str] | dict[str, AdjacentData]
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
        self.stations: List[Station[AdjacentData, TransferData]] = (
            self.__load_stations()
        )

    def __load_stations(self) -> List[Station]:
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

                        new_station = Station(
                            station.name,
                            Location(station.position.lat, station.position.lng),
                            station.route,
                        )

                        new_station.set_closed(station.closed)

                        stations[station_id] = new_station

            for station_data_file in station_data:
                # add adjacent stations
                for station in station_data_file.stations:
                    station_id = f"{station.route}:{station.name}"

                    # check if the adjacent_stations is a list or a dictionary
                    if isinstance(station.adjacent_stations, list):

                        for adjacent_station_id in station.adjacent_stations:
                            if adjacent_station_id not in stations:
                                continue

                            adjacent_station = stations[adjacent_station_id]

                            # Prevent adding the same station as an adjacent station
                            if adjacent_station == stations[station_id]:
                                continue

                            stations[station_id].add_adjacent_station(adjacent_station)
                    else:
                        for (
                            adjacent_station_id,
                            adjacent_station_data,
                        ) in station.adjacent_stations.items():
                            if adjacent_station_id not in stations:
                                continue

                            adjacent_station = stations[adjacent_station_id]

                            # Prevent adding the same station as an adjacent station
                            if adjacent_station == stations[station_id]:
                                continue

                            stations[station_id].add_adjacent_station(
                                adjacent_station, adjacent_station_data
                            )

                # add transfer stations
                for station in station_data_file.stations:
                    station_id = f"{station.route}:{station.name}"
                    for (
                        transfer_station_id,
                        transfer_data,
                    ) in station.transfer_stations.items():
                        if transfer_station_id not in stations:
                            continue

                        transfer_station = stations[transfer_station_id]

                        stations[station_id].add_transfer_station(
                            transfer_station, transfer_data
                        )

            return list(stations.values())

        except (OSError, json.JSONDecodeError) as e:
            print(f"Error loading station data: {e}")
            return []
        except ValidationError as e:
            print(f"Error validating station data: {e}")
            return []
        except Exception as e:
            print(f"An unknown error occurred: {e}")
            return []

    def get_stations_by_route(self, route: str) -> List[Station]:
        """
        Get a list of stations for a specific train line

        :param route: The train line to get stations for
        :return: A list of Station objects
        """
        return [station for station in self.stations if station.route == route]

    def get_station_by_id(self, station_id: str):
        """
        Get a station by ID

        :param station_id: The ID of the station to get
        :return: The Station object
        """
        return next(
            (station for station in self.stations if station.get_id() == station_id),
            None,
        )

    def get_all_stations(self) -> List[Station]:
        return self.stations
