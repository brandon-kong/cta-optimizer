from cta_optimizer.station_data_loader import StationDataLoader, TransferData
from cta_optimizer.stations_graph_service import StationsGraphService
from cta_optimizer.lib.logger import Logger
from cta_optimizer.models.station import Station

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
                "./data/trains/cta/orange_line.json",
            ]
        )

        stations = station_loader.get_all_stations()

        station_graph = StationsGraphService()

        for station in stations:
            station_graph.add_station(station)

        # add edges between adjacent stations
        for station in stations:
            for adjacent_station, _ in station.get_adjacent_stations().items():
                station_graph.add_edge(station, adjacent_station)

            # add transfer stations
            for transfer_station, _ in station.get_transfer_stations().items():
                station_graph.add_edge(station, transfer_station)

        granville_red_line = station_loader.get_station_by_id("yellow:Dempster-Skokie")
        dan_ryan_red_line = station_loader.get_station_by_id("orange:Midway")

        shortest_path = station_graph.get_shortest_path(
            dan_ryan_red_line, granville_red_line
        )

        total_cost = 0
        last_station: Station = None

        for station in shortest_path:
            print(station.get_id())

            if last_station is not None:
                is_transfer: TransferData = last_station.get_transfer_data(station)

                if is_transfer:
                    if not is_transfer.free_transfer:
                        total_cost += 2.50

            last_station = station

        print(f"Total cost of this trip: {total_cost}")

        logger.info("Stations loaded and graph created")

    except Exception as e:
        logger.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
