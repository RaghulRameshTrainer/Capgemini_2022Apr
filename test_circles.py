import unittest
from circles import circle_area
from math import pi

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle_area(1),pi)
        self.assertAlmostEqual(circle_area(0),0)
        self.assertAlmostEqual(circle_area(2.1),pi*(2.1**2))
    def test_areas(self):
        self.assertAlmostEqual(circle_area(2),pi)
    def test_cricleareas(self):
        self.assertAlmostEqual(circle_area(10),pi*100)
