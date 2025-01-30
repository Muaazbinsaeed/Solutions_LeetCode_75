import unittest
from solution import Solution

class TestProductExceptSelf(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_basic_cases(self):
        self.assertEqual(self.s.productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])
        self.assertEqual(self.s.productExceptSelf([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])

    def test_edge_cases(self):
        self.assertEqual(self.s.productExceptSelf([0, 0]), [0, 0])
        self.assertEqual(self.s.productExceptSelf([1]), [1])
        self.assertEqual(self.s.productExceptSelf([-1, -1]), [-1, -1])

    def test_large_input(self):
        nums = [1] * 10**5
        expected_output = [1] * 10**5
        self.assertEqual(self.s.productExceptSelf(nums), expected_output)

if __name__ == "__main__":
    unittest.main()
