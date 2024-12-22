import os
import unittest
from cta_optimizer.station import Station
from cta_optimizer.location import Location

class TestStation(unittest.TestCase):

    def test_station_creates_object(self):
        station = Station("Test Station", Location(0, 0))
        self.assertIsNotNone(station)

    def test_station_with_invalid_name(self):
        with self.assertRaises(ValueError):
            Station(None, Location(0, 0))

        with self.assertRaises(ValueError):
            Station(123, Location(0, 0))

        with self.assertRaises(ValueError):
            Station("", Location(0, 0))

    def test_station_with_invalid_location(self):
        with self.assertRaises(ValueError):
            Station("Test Station", None)

        with self.assertRaises(ValueError):
            Station("Test Station", "Invalid")

    def test_station_add_adjacent_station(self):
        station1 = Station("Station 1", Location(0, 0))
        station2 = Station("Station 2", Location(0, 0))

        station1.add_adjacent_station(station2)
        self.assertIn(station2, station1.get_adjacent_stations())

    def test_station_remove_adjacent_station(self):
        station1 = Station("Station 1", Location(0, 0))
        station2 = Station("Station 2", Location(0, 0))

        station1.add_adjacent_station(station2)
        station1.remove_adjacent_station(station2)
        self.assertNotIn(station2, station1.get_adjacent_stations())

    def test_station_with_invalid_adjacent_station(self):
        station = Station("Test Station", Location(0, 0))
        with self.assertRaises(ValueError):
            station.add_adjacent_station(None)

        with self.assertRaises(ValueError):
            station.add_adjacent_station("Invalid")

        # Test adding the same station as an adjacent station
        with self.assertRaises(ValueError):
            station.add_adjacent_station(station)

    def test_station_get_name(self):
        station = Station("Test Station", Location(0, 0))
        self.assertEqual(station.get_name(), "Test Station")

    def test_station_get_location(self):
        location = Location(0, 0)
        station = Station("Test Station", location)
        self.assertEqual(station.get_location(), location)

    def test_station_equality(self):
        station1 = Station("Test Station", Location(0, 0))
        station2 = Station("Test Station", Location(0, 0))
        station3 = Station("Test Station 2", Location(1, 1))

        self.assertEqual(station1, station2)
        self.assertNotEqual(station1, station3)
        self.assertNotEqual(station2, station3)

        self.assertNotEqual(station1, None)
        self.assertNotEqual(station1, "Invalid")

    def test_station_hash(self):
        station1 = Station("Test Station", Location(0, 0))
        station2 = Station("Test Station", Location(0, 0))
        station3 = Station("Test Station 2", Location(1, 1))

        self.assertEqual(hash(station1), hash(station2))
        self.assertNotEqual(hash(station1), hash(station3))

    def test_station_str(self):
        location = Location(0, 0)
        station = Station("Test Station", location)
        self.assertEqual(str(station), f"Station: Test Station ({location})")