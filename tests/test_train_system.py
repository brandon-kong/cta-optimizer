import unittest

from src.train_system import TrainSystem
from src.train_station import TrainStation
from src.train_line import CTATrainLine

from src.position.position import Position

test_position = Position(latitude=0.0, longitude=-0.0)


class TestTrainSystem(unittest.TestCase):

    def test_train_system_can_be_created(self):
        train_system = TrainSystem()
        self.assertIsInstance(train_system, TrainSystem)

    def test_train_system_add_station(self):
        train_system = TrainSystem()
        train_station = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )

        train_system.add_station(train_station)

        self.assertIn(
            train_station, train_system.get_stations_on_line(CTATrainLine.BLUE)
        )

    def test_train_system_add_station_with_none(self):
        train_system = TrainSystem()

        with self.assertRaises(ValueError) as context:
            train_system.add_station(None)
        self.assertEqual(str(context.exception), "[TrainSystem]: station is required")

    def test_train_system_add_station_with_incorrect_type(self):
        train_system = TrainSystem()

        with self.assertRaises(ValueError) as context:
            train_system.add_station("station")
        self.assertEqual(
            str(context.exception),
            "[TrainSystem]: station must be an instance of TrainStation",
        )

    def test_train_system_get_stations_on_line(self):
        train_system = TrainSystem()
        train_station = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )

        train_system.add_station(train_station)

        self.assertEqual(
            train_system.get_stations_on_line(CTATrainLine.BLUE), [train_station]
        )

    def test_train_system_get_stations_on_line_with_invalid_line(self):
        train_system = TrainSystem()

        with self.assertRaises(ValueError) as context:
            train_system.get_stations_on_line(CTATrainLine.RED)
        self.assertEqual(
            str(context.exception),
            f"[TrainSystem]: {CTATrainLine.RED} line does not exist",
        )
