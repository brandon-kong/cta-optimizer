import unittest

from cta_optimizer.location import Location


class TestLocation(unittest.TestCase):

    def test_location_creates_object(self):
        location = Location(0, 0)
        self.assertIsNotNone(location)

    def test_location_with_invalid_coordinates(self):
        with self.assertRaises(ValueError):
            Location(None, None)

        with self.assertRaises(ValueError):
            Location("Invalid", "Invalid")

        with self.assertRaises(ValueError):
            Location(0, None)

        with self.assertRaises(ValueError):
            Location(0, "Invalid")

    def test_location_invalid_range(self):
        with self.assertRaises(ValueError):
            Location(-91, 0)

        with self.assertRaises(ValueError):
            Location(91, 0)

        with self.assertRaises(ValueError):
            Location(0, -181)

        with self.assertRaises(ValueError):
            Location(0, 181)

    def test_location_get_coordinates(self):
        location = Location(0, 0)
        self.assertEqual(location.get_coordinates(), (0, 0))

    def test_location_get_latitude(self):
        location = Location(0, 0)
        self.assertEqual(location.get_latitude(), 0)

    def test_location_get_longitude(self):
        location = Location(0, 0)
        self.assertEqual(location.get_longitude(), 0)

    def test_location_equality(self):
        location1 = Location(0, 0)
        location2 = Location(0, 0)
        location3 = Location(1, 1)

        self.assertEqual(location1, location2)
        self.assertNotEqual(location1, location3)
        self.assertNotEqual(location2, location3)

        self.assertNotEqual(location1, None)
        self.assertNotEqual(location1, "Invalid")

    def test_location_hash(self):
        location1 = Location(0, 0)
        location2 = Location(0, 0)
        location3 = Location(1, 1)

        self.assertEqual(hash(location1), hash(location2))
        self.assertNotEqual(hash(location1), hash(location3))
        self.assertNotEqual(hash(location2), hash(location3))

        self.assertNotEqual(hash(location1), hash(None))
        self.assertNotEqual(hash(location1), hash("Invalid"))

    def test_location_str(self):
        location = Location(0, 0)
        self.assertEqual(str(location), "Location: 0, 0")
