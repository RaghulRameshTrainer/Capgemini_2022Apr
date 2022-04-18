import unittest
from circles import circle_area
from math import pi

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle_area(1),pi)
        self.assertAlmostEqual(circle_area(0),0)
        self.assertAlmostEqual(circle_area(2.1),pi*(2.1**2))
    def test_areas(self):
        self.assertAlmostEqual(circle_area(2),pi*4)
    def test_cricleareas(self):
        self.assertAlmostEqual(circle_area(10),pi*100)
    def test_values(self):
        self.assertRaises(ValueError,circle_area,-2)
    def test_types(self):
        self.assertRaises(TypeError,circle_area,2+3j)
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, "Python")
    def test_value(self):
        self.assertNotEqual(circle_area(10),pi*4)
