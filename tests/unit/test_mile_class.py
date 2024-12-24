import unittest

from cta_optimizer.models.mile import Mile

class TestMileClass(unittest.TestCase):

    def test_mile_creates_object(self):
        mile = Mile(0)
        self.assertIsNotNone(mile)

    def test_mile_with_invalid_distance(self):
        with self.assertRaises(ValueError):
            Mile(None)

        with self.assertRaises(ValueError):
            Mile("Invalid")

        with self.assertRaises(ValueError):
            Mile(-1)

    def test_mile_to_kilometers(self):
        mile = Mile(1)
        self.assertAlmostEqual(mile.to_kilometers().value, 1.60934, places=5)

    def test_mile_addition(self):
        mile1 = Mile(1)
        mile2 = Mile(2)

        self.assertEqual((mile1 + mile2).value, 3)

    def test_mile_subtraction(self):
        mile1 = Mile(2)
        mile2 = Mile(1)

        self.assertEqual((mile1 - mile2).value, 1)

    def test_mile_equality(self):
        mile1 = Mile(1)
        mile2 = Mile(1)
        mile3 = Mile(2)

        self.assertEqual(mile1, mile2)
        self.assertNotEqual(mile1, mile3)
        self.assertNotEqual(mile2, mile3)

        self.assertNotEqual(mile1, None)
        self.assertNotEqual(mile1, "Invalid")

    def test_mile_hash(self):
        mile = Mile(1)
        self.assertEqual(hash(mile), hash(1))

    def test_mile_to_string(self):
        mile = Mile(1)
        self.assertEqual(str(mile), "1 miles")
