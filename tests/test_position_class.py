import unittest

from src.position import Position


test_position = Position(latitude=0.0, longitude=-0.0)

class TestPositionClass(unittest.TestCase):

    def test_position_can_be_created(self):
        position = Position(latitude=0.0, longitude=-0.0)
        self.assertIsInstance(position, Position)


    def test_position_latitude_is_required(self):
        with self.assertRaises(ValueError) as context:
            Position(longitude=-0.0)
        self.assertEqual(str(context.exception), '[Position]: latitude is required')


    def test_position_latitude_must_be_a_float(self):
        with self.assertRaises(ValueError) as context:
            Position(latitude='latitude', longitude=-0.0)
        self.assertEqual(str(context.exception), '[Position]: latitude must be a float')


    def test_position_longitude_is_required(self):
        with self.assertRaises(ValueError) as context:
            Position(latitude=0.0)
        self.assertEqual(str(context.exception), '[Position]: longitude is required')


    def test_position_longitude_must_be_a_float(self):
        with self.assertRaises(ValueError) as context:
            Position(latitude=0.0, longitude='longitude')
        self.assertEqual(str(context.exception), '[Position]: longitude must be a float')


    def test_position_get_latitude(self):
        position = Position(latitude=0.0, longitude=-0.0)
        self.assertEqual(position.get_latitude(), 0.0)

    
    def test_position_get_longitude(self):
        position = Position(latitude=0.0, longitude=-0.0)
        self.assertEqual(position.get_longitude(), -0.0)


    def test_position_str(self):
        position = Position(latitude=0.0, longitude=-0.0)
        self.assertEqual(str(position), 'Position(latitude=0.0, longitude=-0.0)')