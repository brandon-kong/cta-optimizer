from cta_optimizer.station_data_loader import StationDataLoader
from cta_optimizer.stations_graph_service import StationsGraphService
from cta_optimizer.lib.logger import Logger

from memory_profiler import profile


@profile
def main():

    logger = Logger(
        create_new_file=True,
    )

    try:

        station_loader = StationDataLoader(
            [
                "./data/trains/cta/yellow_line.json",
                "./data/trains/cta/red_line.json",
            ]
        )

        stations = station_loader.get_all_stations()

        print(stations)

        station_graph = StationsGraphService()

        for station in stations:
            station_graph.add_station(station)

        # add edges between stations

        for station in stations:
            for adjacent_station, _ in station.get_adjacent_stations().items():
                station_graph.add_edge(station, adjacent_station)

        granville_red_line = station_loader.get_station_by_id("red:Granville")
        dan_ryan_red_line = station_loader.get_station_by_id("red:95th/Dan Ryan")

        shortest_path = station_graph.get_shortest_path(
            dan_ryan_red_line, granville_red_line
        )

        for station in shortest_path:
            print(station.get_name())

        logger.info("Stations loaded and graph created")

    except Exception as e:
        logger.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
