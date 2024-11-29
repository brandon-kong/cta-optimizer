import unittest

from src.position.position_factory import PositionFactory


class TestPositionFactory(unittest.TestCase):

    def test_position_factory_creates_positions(self):
        position = PositionFactory.get_position(latitude=0.0, longitude=-0.0)
        self.assertIsNotNone(position)

    def test_position_factory_retrieves_positions(self):
        position = PositionFactory.get_position(latitude=0.0, longitude=-0.0)
        same_position = PositionFactory.get_position(latitude=0.0, longitude=-0.0)

        self.assertEqual(position, same_position)

    def test_position_factory_stores_positions(self):
        position = PositionFactory.get_position(latitude=0.0, longitude=-0.0)
        same_position = PositionFactory.get_position(latitude=0.0, longitude=-0.0)

        self.assertIs(position, same_position)