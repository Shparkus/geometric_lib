import unittest
from rectangle import *
from math import pi

class RectangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_area_minus(self):
        with self.assertRaises(TypeError):
            res = area(-5, 5)

    def test_area_square(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_area_random(self):
        res = area(23, 15)
        self.assertEqual(res, 345)

    def test_area_random_big(self):
        res = area(1789594, 1326458)
        self.assertEqual(res, 2373821278052)

    def test_area_string(self):
        with self.assertRaises(TypeError):
            res = area("a", 15)

    def test_area_string_both(self):
        with self.assertRaises(TypeError):
            res = area("b", "a")
        
    def test_area_underscore_number(self):
        res = area(5_000, 10)
        self.assertEqual(res, 50000)

    def test_area_double(self):
        res = area(1.78932156, 3)
        self.assertEqual(res, 5.36796468)

    def test_area_pi(self):
        res = area(pi,3)
        self.assertEqual(res, 9.42477796076938)

    def test_perimeter_zero(self):
        res = perimeter(10, 0)
        self.assertEqual(res, 20)

    def test_perimeter_minus(self):
        with self.assertRaises(TypeError):
            res = perimeter(-5, 5)

    def test_perimeter_square(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_perimeter_random(self):
        res = perimeter(23, 15)
        self.assertEqual(res, 76)

    def test_perimeter_random_big(self):
        res = perimeter(1789594, 1326458)
        self.assertEqual(res, 6232104)

    def test_perimeter_string(self):
        with self.assertRaises(TypeError):
            res = perimeter("a", 15)

    def test_perimeter_string_both(self):
        with self.assertRaises(TypeError):
            res = perimeter("b", "a")
        
    def test_perimeter_underscore_number(self):
        res = perimeter(5_000, 10)
        self.assertEqual(res, 10020)

    def test_perimeter_double(self):
        res = perimeter(1.78932156, 3)
        self.assertEqual(res, 9.57864312)

    def test_perimeter_pi(self):
        res = perimeter(pi,3)
        self.assertEqual(res, 12.283185307179586)

        
