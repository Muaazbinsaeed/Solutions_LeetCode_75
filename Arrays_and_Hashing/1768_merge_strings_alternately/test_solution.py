import unittest
from solution import Solution
# from . import Solution 

class TestMergeStringsAlternately(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_basic_cases(self):
        self.assertEqual(self.s.mergeAlternately("abc", "pqr"), "apbqcr")
        self.assertEqual(self.s.mergeAlternately("ab", "pqrs"), "apbqrs")
        self.assertEqual(self.s.mergeAlternately("abcd", "pq"), "apbqcd")

    def test_one_empty_string(self):
        # Edge case if one string is empty (if it were allowed in constraints)
        self.assertEqual(self.s.mergeAlternately("", "pqrs"), "pqrs")
        self.assertEqual(self.s.mergeAlternately("abcd", ""), "abcd")

    def test_same_length(self):
        self.assertEqual(self.s.mergeAlternately("ab", "cd"), "acbd")

if __name__ == "__main__":
    unittest.main()
