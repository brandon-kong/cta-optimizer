import json

from cta_optimizer.station_data_loader import TransferData
from pydantic import BaseModel


class Location(BaseModel):
    latitude: float
    longitude: float

class Position(BaseModel):
    lat: float
    lng: float

class RawStationData(BaseModel):
    stop_name: str
    station_name: str
    red: bool
    blue: bool
    g: bool
    brn: bool
    p: bool
    pexp: bool
    y: bool
    pnk: bool
    o: bool

    location: Location


class FormattedStationData(BaseModel):
    name: str
    closed: bool = False
    route: str
    position: Position
    adjacent_stations: list[str]
    transfer_stations: dict[str, TransferData]


def main():
    # Read the raw CTA stations data
    with open("../../data/trains/cta/stations.json", "r") as file:
        raw_station_data = json.load(file)

    # Parse the raw CTA stations data
    parsed_station_data = []

    for station in raw_station_data:
        parsed_station_data.append(
            RawStationData(
                **station
            )
        )

    red_line_stations = list(filter(lambda x: x.red, parsed_station_data))
    blue_line_stations = list(filter(lambda x: x.blue, parsed_station_data))
    green_line_stations = list(filter(lambda x: x.g, parsed_station_data))
    brown_line_stations = list(filter(lambda x: x.brn, parsed_station_data))
    purple_line_stations = list(filter(lambda x: x.p, parsed_station_data))
    purple_express_line_stations = list(filter(lambda x: x.pexp, parsed_station_data))
    yellow_line_stations = list(filter(lambda x: x.y, parsed_station_data))
    pink_line_stations = list(filter(lambda x: x.pnk, parsed_station_data))
    orange_line_stations = list(filter(lambda x: x.o, parsed_station_data))

    lines = {
        "red": red_line_stations,
        "blue": blue_line_stations,
        "green": green_line_stations,
        "brown": brown_line_stations,
        "purple": purple_line_stations,
        "purple_express": purple_express_line_stations,
        "yellow": yellow_line_stations,
        "pink": pink_line_stations,
        "orange": orange_line_stations,
    }

    # Format the CTA stations data
    formatted_station_data = []

    for line, stations in lines.items():
        for station in stations:
            formatted_station_data.append(
                FormattedStationData(
                    name=station.station_name,
                    route=line,
                    position=Position(
                        lat=station.location.latitude,
                        lng=station.location.longitude
                    ),
                    adjacent_stations=[],
                    transfer_stations={}
                )
            )



    # Write the formatted CTA stations data
    with open("../../data/trains/cta/formatted_stations.json", "w") as file:
        json.dump(
            formatted_station_data,
            file,
            indent=4,
            default=lambda x: x.model_dump()
        )

    # split the formatted stations data into separate files
    for line, stations in lines.items():
        line_stations = list(filter(lambda x: x.route == line, formatted_station_data))
        # remove duplicates from each line
        line_stations = list({station.name: station for station in line_stations}.values())

        with open(f"../../data/trains/cta/{line}_line.json", "w") as file:
            json.dump(
                line_stations,
                file,
                indent=4,
                default=lambda x: x.model_dump()
            )



if __name__ == "__main__":
    main()