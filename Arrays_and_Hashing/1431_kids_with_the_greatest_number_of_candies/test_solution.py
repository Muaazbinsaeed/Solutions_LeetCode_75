import unittest
from solution import Solution

class TestKidsWithCandies(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_basic_cases(self):
        self.assertEqual(
            self.s.kidsWithCandies([2, 3, 5, 1, 3], 3), 
            [True, True, True, False, True]
        )
        self.assertEqual(
            self.s.kidsWithCandies([4, 2, 1, 1, 2], 1), 
            [True, False, False, False, False]
        )
        self.assertEqual(
            self.s.kidsWithCandies([12, 1, 12], 10), 
            [True, False, True]
        )

    def test_all_equal(self):
        # Case where all kids have the same candies
        self.assertEqual(
            self.s.kidsWithCandies([5, 5, 5, 5], 0), 
            [True, True, True, True]
        )

    def test_extra_candies_zero(self):
        # Case where extraCandies is zero
        self.assertEqual(
            self.s.kidsWithCandies([1, 2, 3], 0), 
            [False, False, True]
        )

    def test_large_input(self):
        # Large input test
        candies = [10**6] * 100
        self.assertEqual(
            self.s.kidsWithCandies(candies, 0), 
            [True] * 100
        )

if __name__ == "__main__":
    unittest.main()
