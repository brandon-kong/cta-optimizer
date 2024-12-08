import unittest

from src.train_station import TrainStation, TrainTransfer, TrainAction
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

        transfer = TrainTransfer(source=train_station, destination=transfer_station)

        train_station.add_transfer_station(transfer)
        self.assertEqual(train_station.get_transfer_stations(), [transfer])

    def test_train_station_add_transfer_station_raises_error_if_station_is_none(self):
        train_station = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )

        with self.assertRaises(ValueError) as context:
            train_station.add_transfer_station(None)
        self.assertEqual(str(context.exception), "[TrainStation]: station is required")

    def test_train_station_add_transfer_station_raises_error_if_station_is_not_instance_of_train_transfer(
        self,
    ):
        train_station = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )

        with self.assertRaises(ValueError) as context:
            train_station.add_transfer_station("station")
        self.assertEqual(
            str(context.exception),
            "[TrainStation]: station must be an instance of TrainTransfer",
        )

    def test_train_station_get_transfer_stations(self):
        train_station = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )
        transfer_station = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )

        transfer = TrainTransfer(source=train_station, destination=transfer_station)

        train_station.add_transfer_station(transfer)
        self.assertEqual(train_station.get_transfer_stations(), [transfer])

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

    def test_train_station_get_id(self):
        train_station = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )
        self.assertEqual(train_station.get_id(), "blue:name")

    def test_train_station_hash(self):
        train_station = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )
        self.assertEqual(
            hash(
                (
                    train_station.get_name(),
                    train_station.get_line(),
                    train_station.get_position(),
                )
            ),
            hash(train_station),
        )


class TestTrainAction(unittest.TestCase):
    def test_train_transfer_can_be_created(self):
        source = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )

        destination = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )

        train_action = TrainAction(source=source)
        self.assertIsInstance(train_action, TrainAction)

    def test_train_action_source_is_required(self):
        with self.assertRaises(ValueError) as context:
            TrainAction(source=None)
        self.assertEqual(str(context.exception), "[TrainAction]: source is required")

    def test_train_action_source_must_be_an_instance_of_train_station(self):
        with self.assertRaises(ValueError) as context:
            TrainAction(source="source")
        self.assertEqual(
            str(context.exception),
            "[TrainAction]: source must be an instance of TrainStation",
        )

    def test_train_action_cost_is_zero_by_default(self):
        source = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )
        train_action = TrainAction(source=source)
        self.assertEqual(train_action.get_cost(), 0.0)

    def test_train_action_cost_must_be_a_float(self):
        source = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )

        with self.assertRaises(ValueError) as context:
            TrainAction(source=source, cost="cost")
        self.assertEqual(str(context.exception), "[TrainAction]: cost must be a float")

    def test_train_action_get_source(self):
        source = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )
        train_action = TrainAction(source=source)
        self.assertEqual(train_action.get_source(), source)

    def test_train_action_get_cost(self):
        source = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )
        train_action = TrainAction(source=source, cost=1.0)
        self.assertEqual(train_action.get_cost(), 1.0)

    def test_train_action_str(self):
        source = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )
        train_action = TrainAction(source=source)
        self.assertEqual(str(train_action), f"Action[ {source} ]")


class TestTrainTransfer(unittest.TestCase):
    def test_train_transfer_can_be_created(self):
        source = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )
        destination = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )

        train_transfer = TrainTransfer(source=source, destination=destination)
        self.assertIsInstance(train_transfer, TrainTransfer)

    def test_train_transfer_source_is_required(self):
        destination = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )

        with self.assertRaises(ValueError):
            TrainTransfer(source=None, destination=destination)

    def test_train_transfer_source_must_be_an_instance_of_train_station(self):
        destination = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )

        with self.assertRaises(ValueError):
            TrainTransfer(source="source", destination=destination)

    def test_train_transfer_destination_is_required(self):
        source = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )

        with self.assertRaises(ValueError) as context:
            TrainTransfer(source=source, destination=None)
        self.assertEqual(
            str(context.exception), "[TrainTransfer]: destination is required"
        )

    def test_train_transfer_destination_must_be_an_instance_of_train_station(self):
        source = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )

        with self.assertRaises(ValueError) as context:
            TrainTransfer(source=source, destination="destination")
        self.assertEqual(
            str(context.exception),
            "[TrainTransfer]: destination must be an instance of TrainStation",
        )

    def test_train_transfer_get_source(self):
        source = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )
        destination = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )

        train_transfer = TrainTransfer(source=source, destination=destination)
        self.assertEqual(train_transfer.get_source(), source)

    def test_train_transfer_get_destination(self):
        source = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )

        destination = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )

        train_transfer = TrainTransfer(source=source, destination=destination)
        self.assertEqual(train_transfer.get_destination(), destination)

    def test_train_transfer_str(self):
        source = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )

        destination = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )

        train_transfer = TrainTransfer(source=source, destination=destination)
        self.assertEqual(str(train_transfer), f"Transfer[ {source} -> {destination} ]")

    def test_train_transfer_is_transfer_paid(self):
        source = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )

        destination = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )

        train_transfer = TrainTransfer(source=source, destination=destination)
        self.assertFalse(train_transfer.is_transfer_paid())

        paid_transfer = TrainTransfer(
            source=source, destination=destination, is_paid=True
        )
        self.assertTrue(paid_transfer.is_transfer_paid())

    def test_train_transfer_is_same_line(self):
        source = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )

        destination = TrainStation(
            name="name", line=CTATrainLine.BLUE, position=test_position
        )

        train_transfer = TrainTransfer(source=source, destination=destination)
        self.assertTrue(train_transfer.is_same_line())

        different_line_destination = TrainStation(
            name="name", line=CTATrainLine.RED, position=test_position
        )

        different_line_transfer = TrainTransfer(
            source=source, destination=different_line_destination
        )
        self.assertFalse(different_line_transfer.is_same_line())
