from typing import List

from cta_optimizer.station_data_loader import StationDataLoader
from cta_optimizer.models.station import Station
from cta_optimizer.cta.train_station import (
    CTATrainLine
)


class CTAStationDataLoader(StationDataLoader):
    def __init__(self, files: List[str] = None):
        super().__init__(files)

    def get_stations_by_route(self, line: CTATrainLine) -> List[Station]:
        """
        Get a list of stations for a specific train line

        :param line: The train line to get stations for
        :return: A list of Station objects
        """
        return [station for station in self.stations if station.route == line.value.lower()]

