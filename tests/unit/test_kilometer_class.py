import unittest

from cta_optimizer.models.kilometer import Kilometer


class TestKilometerClass(unittest.TestCase):

    def test_kilometer_creates_object(self):
        kilometer = Kilometer(0)
        self.assertIsNotNone(kilometer)

    def test_kilometer_with_invalid_distance(self):
        with self.assertRaises(ValueError):
            Kilometer(None)

        with self.assertRaises(ValueError):
            Kilometer("Invalid")

        with self.assertRaises(ValueError):
            Kilometer(-1)

    def test_kilometer_to_miles(self):
        kilometer = Kilometer(1)
        self.assertEqual(kilometer.to_miles().value, 0.621371)

    def test_kilometer_addition(self):
        kilometer1 = Kilometer(1)
        kilometer2 = Kilometer(2)

        self.assertEqual((kilometer1 + kilometer2).value, 3)

    def test_kilometer_subtraction(self):
        kilometer1 = Kilometer(2)
        kilometer2 = Kilometer(1)

        self.assertEqual((kilometer1 - kilometer2).value, 1)

    def test_kilometer_equality(self):
        kilometer1 = Kilometer(1)
        kilometer2 = Kilometer(1)
        kilometer3 = Kilometer(2)

        self.assertEqual(kilometer1, kilometer2)
        self.assertNotEqual(kilometer1, kilometer3)
        self.assertNotEqual(kilometer2, kilometer3)

        self.assertNotEqual(kilometer1, None)
        self.assertNotEqual(kilometer1, "Invalid")

    def test_kilometer_hash(self):
        kilometer = Kilometer(1)
        self.assertEqual(hash(kilometer), hash(1))

    def test_kilometer_to_string(self):
        kilometer = Kilometer(1)
        self.assertEqual(str(kilometer), "1 km")
