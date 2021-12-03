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
        self.assertEqual("0", calculate_params({ "0": 100, "1": 0 }, True, "0"))
        self.assertEqual("1", calculate_params({ "0": 100, "1": 0 }, False, "0"))
        self.assertEqual("1", calculate_params({ "0": 100, "1": 100 }, False, "1"))
        self.assertEqual("1", calculate_params({ "0": 100, "1": 100 }, True, "1"))

    def test_filter_input(self):
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

        expected_input = [
            "11110",
            "10110",
            "10111",
            "10101",
            "11100",
            "10000",
            "11001",
        ]
        self.assertEqual(expected_input, filter_input(input, 0, "1"))

    def test_calculate_oxygen(self):
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

        self.assertEqual("10111", calculate_oxygen(input))

    def test_calculate_co2(self):
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
            
        self.assertEqual("01010", calculate_co2(input))

    def test_calculate_life_support_rating(self):
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
        self.assertEqual(230, calculate_life_support_rating(input))

if __name__ == '__main__':
    unittest.main()