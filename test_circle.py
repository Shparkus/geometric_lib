import unittest
from circle import *

class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_minus(self):
        with self.assertRaises(TypeError):
            res = area(-5)

    def test_area_random(self):
        res = area(178596)
        self.assertEqual(res, 100205908143.18312)

    def test_area_string(self):
        with self.assertRaises(TypeError):
            res = area("a")

    def test_area_double(self):
        res = area(1.45)
        self.assertEqual(res, 6.6051985541725395)

    def test_area_underscore_number(self):
        res = area(178_596)
        self.assertEqual(res, 100205908143.18312)

    def test_perimeter_random(self):
        res = perimeter(178596)
        self.assertEqual(res, 1122151.7631210454)

    def test_perimeter_minus(self):
        with self.assertRaises(TypeError):
            res = perimeter(-5)

    def test_perimeter_string(self):
        with self.assertRaises(TypeError):
            res = perimeter("a")

    def test_perimeter_double(self):
        res = perimeter(1.45)
        self.assertEqual(res, 9.1106186954104)

    def test_perimeter_underscore_number(self):
        res = perimeter(178_596)
        self.assertEqual(res, 1122151.7631210454)
