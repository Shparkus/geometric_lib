import unittest
from triangle import *

class TriangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(100, 0)
        self.assertEqual(res, 0)

    def test_area_random(self):
        res = area(123458, 12)
        self.assertEqual(res, 740748)

    def test_area_random_big(self):
        res = area(123456789, 98765)
        self.assertEqual(res, 6096604882792.5)

    def test_area_string(self):
        res = area("134", 10)
        self.assertEqual(res, "Illegal argument")

    def test_area_double(self):
        res = area(1.78965, 4)
        self.assertEqual(res, 3.5793)

    def test_area_underscore_number(self):
        res = area(4_000,78)
        self.assertEqual(res, 156000)

    def test_perimeter_zero(self):
        res = perimeter(100, 0, 5)
        self.assertEqual(res, "Wrong argument")

    def test_perimeter_random(self):
        res = perimeter(126789, 132467, 159256)
        self.assertEqual(res, 418512)

    def test_perimeter_random_wrong(self):
        res = perimeter(126789, 132467, 359256)
        self.assertEqual(res, "Wrong argument")

    def test_perimeter_string(self):
        res = perimeter("134", 100, 50)
        self.assertEqual(res, "Illegal argument")

    def test_perimeter_underscore_number(self):
        res = perimeter(126_789, 132467, 159256)
        self.assertEqual(res, 418512)
        
