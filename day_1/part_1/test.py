import unittest
from main import *


class TestSum(unittest.TestCase):
    def test_check_increasing_depths(self):
        depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        self.assertEqual(check_increasing_depths(depths), 7)

if __name__ == '__main__':
    unittest.main()