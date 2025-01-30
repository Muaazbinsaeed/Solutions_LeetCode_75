import unittest
from solution import Solution

class TestIncreasingTriplet(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_basic_cases(self):
        self.assertEqual(self.s.increasingTriplet([1, 2, 3, 4, 5]), True)
        self.assertEqual(self.s.increasingTriplet([5, 4, 3, 2, 1]), False)
        self.assertEqual(self.s.increasingTriplet([2, 1, 5, 0, 4, 6]), True)

    def test_edge_cases(self):
        self.assertEqual(self.s.increasingTriplet([1, 1, 1, 1, 1]), False)
        self.assertEqual(self.s.increasingTriplet([20, 100, 10, 12, 5, 13]), True)
        self.assertEqual(self.s.increasingTriplet([2, 3, 2, 3, 2, 3, 4]), True)

    def test_large_input(self):
        nums = list(range(10**5))
        self.assertEqual(self.s.increasingTriplet(nums), True)

if __name__ == "__main__":
    unittest.main()
