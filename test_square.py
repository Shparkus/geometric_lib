import unittest
from square import *

class SquareTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_random(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_area_random_big(self):
        res = area(1789594)
        self.assertEqual(res, 3202646684836)

    def test_area_string(self):
        res = area("a")
        self.assertEqual(res, "Illegal argument")

    def test_area_string_number(self):
        res = area("1")
        self.assertEqual(res, "Illegal arguments")
        
    def test_area_underscore_number(self):
        res = area(5_000)
        self.assertEqual(res, 25000000)

    def test_area_double(self):
        res = area(1.78)
        self.assertEqual(res, 3.1684)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_random_big(self):
        res = perimeter(1789594)
        self.assertEqual(res, 7158376)

    def test_perimeter_string(self):
        res = perimeter("a")
        self.assertEqual(res, "Illegal argument")

    def test_perimeter_string_number(self):
        res = perimeter("1")
        self.assertEqual(res, "Illegal arguments")
        
    def test_perimeter_underscore_number(self):
        res = perimeter(5_000)
        self.assertEqual(res, 20000)

    def test_perimeter_double(self):
        res = perimeter(1.78932156)
        self.assertEqual(res, 7.15728624)
        
