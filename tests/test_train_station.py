import unittest

from src.train_station import TrainStation
from src.train_line import CTATrainLine
from src.position.position import Position


test_position = Position(latitude=0.0, longitude=-0.0)


class TestTrainStation(unittest.TestCase):

    def test_train_station_can_be_created(self):
        train_station = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )
        self.assertIsInstance(train_station, TrainStation)

    def test_train_station_name_is_required(self):
        with self.assertRaises(ValueError) as context:
            TrainStation(line=CTATrainLine.BLUE, position=test_position)
        self.assertEqual(str(context.exception), "[TrainStation]: name is required")

    def test_train_station_name_must_be_a_string(self):
        with self.assertRaises(ValueError) as context:
            TrainStation(name=True, line=CTATrainLine.BLUE, position=test_position)
        self.assertEqual(
            str(context.exception), "[TrainStation]: name must be a string"
        )

    def test_train_station_position_is_required(self):
        with self.assertRaises(ValueError) as context:
            TrainStation(name="name", line=CTATrainLine.BLUE)
        self.assertEqual(str(context.exception), "[TrainStation]: position is required")

    def test_train_station_position_must_be_an_instance_of_position(self):
        with self.assertRaises(ValueError) as context:
            TrainStation(name="name", line=CTATrainLine.BLUE, position="position")
        self.assertEqual(
            str(context.exception),
            "[TrainStation]: position must be an instance of Position",
        )

    def test_train_station_line_must_be_an_instance_of_CTATrainLine(self):
        with self.assertRaises(ValueError) as context:
            TrainStation(name="name", line="line", position=test_position)
        self.assertEqual(
            str(context.exception), "[TrainStation]: line must be a string"
        )

    def test_train_station_get_name(self):
        train_station = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )
        self.assertEqual(train_station.get_name(), "name")

    def test_train_station_get_position(self):
        train_station = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )
        self.assertEqual(train_station.get_position(), test_position)

    def test_train_station_get_line(self):
        train_station = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )

        self.assertEqual(train_station.get_line(), CTATrainLine.BLUE)

    def test_train_station_add_transfer_station(self):
        train_station = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )
        transfer_station = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )

        train_station.add_transfer_station(transfer_station)
        self.assertEqual(train_station.get_transfer_stations(), [transfer_station])

    def test_train_station_add_transfer_station_raises_error_if_station_is_none(self):
        train_station = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )

        with self.assertRaises(ValueError) as context:
            train_station.add_transfer_station(None)
        self.assertEqual(str(context.exception), "[TrainStation]: station is required")

    def test_train_station_add_transfer_station_raises_error_if_station_is_not_instance_of_train_station(
        self,
    ):
        train_station = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )

        with self.assertRaises(ValueError) as context:
            train_station.add_transfer_station("station")
        self.assertEqual(
            str(context.exception),
            "[TrainStation]: station must be an instance of TrainStation",
        )

    def test_train_station_get_transfer_stations(self):
        train_station = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )
        transfer_station = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )

        train_station.add_transfer_station(transfer_station)
        self.assertEqual(train_station.get_transfer_stations(), [transfer_station])

    def test_train_station_str(self):
        train_station = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )
        self.assertEqual(
            str(train_station), f"{train_station.get_name()} ({train_station.line})"
        )

    def test_train_station_equals(self):
        train_station = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )
        other_train_station = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )

        self.assertEqual(train_station, other_train_station)

    def test_train_station_not_equals(self):
        train_station = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )
        other_train_station = TrainStation(
            name="name", line=CTATrainLine.RED, position=test_position
        )

        self.assertNotEqual(train_station, other_train_station)

        # Test with None
        self.assertNotEqual(train_station, None)

        # Test with different type
        self.assertNotEqual(train_station, "train_station")

    def test_train_station_close(self):
        train_station = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )
        train_station.close()
        self.assertFalse(train_station.is_station_open())

    def test_train_station_open(self):
        train_station = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )
        train_station.close()
        train_station.open()
        self.assertTrue(train_station.is_station_open())

    def test_train_station_is_station_open(self):
        train_station = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )
        self.assertTrue(train_station.is_station_open())

        train_station.close()
        self.assertFalse(train_station.is_station_open())
