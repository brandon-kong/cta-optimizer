from cta_optimizer.station_data_loader import StationDataLoader
from cta_optimizer.stations_graph_service import StationsGraphService

from cta_optimizer.lib.logger import Logger

def main():

    logger = Logger(
        create_new_file=True,
    )

    station_loader = StationDataLoader([
        "./data/trains/cta/yellow_line.json",
        "./data/trains/cta/red_line.json",
    ])

    stations = station_loader.get_all_stations()

    station_graph = StationsGraphService()

    for station in stations:
        station_graph.add_station(station)

    # add edges between stations

    for station in stations:
        for adjacent_station, _ in station.get_adjacent_stations().items():
            print(f"Adding edge between {station} and {adjacent_station}")
            station_graph.add_edge(station, adjacent_station)

    logger.info("Stations loaded and graph created")


if __name__ == "__main__":
    main()