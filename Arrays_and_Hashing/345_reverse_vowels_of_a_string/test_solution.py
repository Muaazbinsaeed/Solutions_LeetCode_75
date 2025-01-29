import unittest
from solution import Solution

class TestReverseVowels(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_basic_cases(self):
        self.assertEqual(self.s.reverseVowels("hello"), "holle")
        self.assertEqual(self.s.reverseVowels("leetcode"), "leotcede")

    def test_all_vowels(self):
        self.assertEqual(self.s.reverseVowels("aeiou"), "uoiea")
        self.assertEqual(self.s.reverseVowels("AEIOU"), "UOIEA")

    def test_no_vowels(self):
        self.assertEqual(self.s.reverseVowels("bcdfg"), "bcdfg")

    def test_mixed_cases(self):
        self.assertEqual(self.s.reverseVowels("hElLo"), "holLE")
        self.assertEqual(self.s.reverseVowels("AbcdeO"), "ObcdeA")

    def test_single_character(self):
        self.assertEqual(self.s.reverseVowels("a"), "a")
        self.assertEqual(self.s.reverseVowels("z"), "z")

    def test_large_input(self):
        self.assertEqual(self.s.reverseVowels("a" * 10**5 + "e"), "e" + "a" * 10**5)

if __name__ == "__main__":
    unittest.main()
