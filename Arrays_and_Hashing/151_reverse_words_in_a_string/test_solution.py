import unittest
from solution import Solution

class TestReverseWords(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_basic_cases(self):
        self.assertEqual(self.s.reverseWords("the sky is blue"), "blue is sky the")
        self.assertEqual(self.s.reverseWords("  hello world  "), "world hello")
        self.assertEqual(self.s.reverseWords("a good   example"), "example good a")

    def test_edge_cases(self):
        self.assertEqual(self.s.reverseWords("   a   b "), "b a")  # Multiple spaces
        self.assertEqual(self.s.reverseWords("single"), "single")  # Single word
        self.assertEqual(self.s.reverseWords("   "), "")  # Only spaces

    def test_mixed_case_and_numbers(self):
        self.assertEqual(self.s.reverseWords("Muaaz is amazing"), "amazing is Muaaz")
        self.assertEqual(self.s.reverseWords("123 456 789"), "789 456 123")
        self.assertEqual(self.s.reverseWords("HELLO world"), "world HELLO")

if __name__ == "__main__":
    unittest.main()
