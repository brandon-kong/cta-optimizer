import unittest

from cta_optimizer.station_data_loader import StationDataLoader

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

    def test_data_loader_loads_data(self):
        data_loader = StationDataLoader(["../data/trains/cta/yellow_line.json"])
        stations = data_loader.get_all_stations()

        self.assertIsNotNone(stations)


