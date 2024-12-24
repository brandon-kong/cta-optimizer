import unittest
from unittest.mock import patch
from pydantic import ValidationError

from cta_optimizer.station_data_loader import StationDataLoader

mock_json_data = {
    "route_name": "yellow",
    "speed": 25,
    "stations": [
        {
            "name": "Dempster-Skokie",
            "route": "yellow",
            "position": {"lat": 42.038951, "lng": -87.751919},
            "adjacent_stations": ["red:Howard"],
            "transfer_stations": {},
        }
    ],
}


class TestStationDataLoader(unittest.TestCase):

    def test_data_loader_creates_object(self):
        data_loader = StationDataLoader(["../data/trains/cta/yellow_line.json"])
        self.assertIsNotNone(data_loader)

    def test_data_loader_with_invalid_filename(self):
        with self.assertRaises(ValueError):
            StationDataLoader(None)

        with self.assertRaises(ValueError):
            StationDataLoader(123)

        with self.assertRaises(ValueError):
            StationDataLoader("")

        with self.assertRaises(ValueError):
            StationDataLoader([])

    def test_data_loader_loads_data(self):
        data_loader = StationDataLoader(["../data/trains/cta/yellow_line.json"])
        stations = data_loader.get_all_stations()

        self.assertIsNotNone(stations)

    def test_data_loader_get_station_by_id(self):
        data_loader = StationDataLoader(["../data/trains/cta/yellow_line.json"])
        station = data_loader.get_station_by_id("yellow:Dempster-Skokie")

        self.assertIsNotNone(station)
        self.assertEqual(station.get_name(), "Dempster-Skokie")

    def test_data_loader_get_station_by_invalid_id(self):
        data_loader = StationDataLoader(["../data/trains/cta/yellow_line.json"])
        station = data_loader.get_station_by_id("yellow:Invalid")

        self.assertIsNone(station)

    def test_data_loader_get_stations_by_route(self):
        data_loader = StationDataLoader(["../data/trains/cta/yellow_line.json"])
        stations = data_loader.get_stations_by_route("yellow")

        self.assertIsNotNone(stations)
        self.assertGreater(len(stations), 0)

    @patch("builtins.open", side_effect=OSError())
    def test_data_loader_open_file_error(self, mock_json_load):
        data_loader = StationDataLoader(["../data/trains/cta/yellow_line.json"])

        self.assertEqual(data_loader.get_all_stations(), [])

    @patch("builtins.open", side_effect=ValidationError("Invalid data", []))
    def test_data_loader_validation_error(self, mock_station_data):
        data_loader = StationDataLoader(["../data/trains/cta/yellow_line.json"])
        data_loader._validate_station_data = lambda x: None

        self.assertEqual(data_loader.get_all_stations(), [])

    @patch("builtins.open", side_effect=Exception)
    def test_data_loader_unknown_error(self, mock_station_data):
        data_loader = StationDataLoader(["../data/trains/cta/yellow_line.json"])
        data_loader._validate_station_data = lambda x: None

        self.assertEqual(data_loader.get_all_stations(), [])

    @patch("json.load", return_value=mock_json_data)
    def test_data_loader_load_invalid_adjacent_station(self, mock_json_load):
        data_loader = StationDataLoader(["../data/trains/cta/yellow_line.json"])
        stations = data_loader.get_all_stations()

        self.assertIsNotNone(stations)
        self.assertEqual(len(stations), 1)

        station = stations[0]
        self.assertEqual(len(station.get_adjacent_stations().keys()), 0)
