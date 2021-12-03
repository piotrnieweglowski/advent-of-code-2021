import unittest
from main import *


class TestSum(unittest.TestCase):
    def test_calculate_chars(self):
        input = [
            "00100",
            "11110",
            "10110",
            "10111",
            "10101",
            "01111",
            "00111",
            "11100",
            "10000",
            "11001",
            "00010",
            "01010"
            ]

        count = calculate_chars(input, 0)
        self.assertEqual(5, count["0"])
        self.assertEqual(7, count["1"])

    def test_calculate_params(self):
        e1, g1 = calculate_params({ "0": 100, "1": 0 })
        e2, g2 = calculate_params({ "0": 0, "1": 100 })
        self.assertEqual(e1, "0")
        self.assertEqual(g1, "1")
        self.assertEqual(e2, "1")
        self.assertEqual(g2, "0")

    def test_calculate_power_consumption(self):
        input = [
            "00100",
            "11110",
            "10110",
            "10111",
            "10101",
            "01111",
            "00111",
            "11100",
            "10000",
            "11001",
            "00010",
            "01010"
            ]
        self.assertEqual(198, calculate_power_consumption(input))

if __name__ == '__main__':
    unittest.main()