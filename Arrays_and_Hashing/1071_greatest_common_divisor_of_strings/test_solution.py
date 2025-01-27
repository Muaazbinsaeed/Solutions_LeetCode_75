import unittest
from solution import Solution

class TestGCDOfStrings(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_basic_cases(self):
        # Example cases from the problem statement
        self.assertEqual(self.s.gcdOfStrings("ABCABC", "ABC"), "ABC")
        self.assertEqual(self.s.gcdOfStrings("ABABAB", "ABAB"), "AB")
        self.assertEqual(self.s.gcdOfStrings("LEET", "CODE"), "")

    def test_one_string_is_empty(self):
        # Edge case where one string is empty
        self.assertEqual(self.s.gcdOfStrings("", "ABC"), "")
        self.assertEqual(self.s.gcdOfStrings("ABC", ""), "")

    def test_no_common_divisor(self):
        # Cases where there is no common divisor
        self.assertEqual(self.s.gcdOfStrings("ABCD", "EFGH"), "")
        self.assertEqual(self.s.gcdOfStrings("A", "B"), "")

    def test_same_strings(self):
        # Case where both strings are identical
        self.assertEqual(self.s.gcdOfStrings("ABC", "ABC"), "ABC")
        self.assertEqual(self.s.gcdOfStrings("AAAA", "AAAA"), "AAAA")

    def test_one_string_is_multiple_of_another(self):
        # Case where one string is a repeated version of another
        self.assertEqual(self.s.gcdOfStrings("ABABAB", "AB"), "AB")
        self.assertEqual(self.s.gcdOfStrings("XYZXYZ", "XYZ"), "XYZ")

    def test_large_inputs(self):
        # Testing performance with larger inputs
        self.assertEqual(self.s.gcdOfStrings("A" * 1000, "A" * 500), "A" * 500)
        self.assertEqual(self.s.gcdOfStrings("AB" * 500, "AB" * 250), "AB" * 250)

if __name__ == "__main__":
    unittest.main()
