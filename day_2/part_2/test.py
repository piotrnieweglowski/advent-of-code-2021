import unittest
from main import *


class TestSum(unittest.TestCase):
    def test_calculate_position(self):
        moves = [
            "forward 5",
            "down 5",
            "forward 8",
            "up 3",
            "down 8",
            "forward 2"
            ]

        depth, horizontal = calculate_position(moves)
        self.assertEqual(horizontal, 15)
        self.assertEqual(depth, 60)

if __name__ == '__main__':
    unittest.main()