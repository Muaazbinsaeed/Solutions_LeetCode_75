import unittest
# from Sol import Solution 
from . import Solution 

class TestSolution(unittest.TestCase):
    def test_sol(self):
        s = Solution()
        self.assertEqual(s.mergeAlternately(word1 = "abc", word2 = "pqr"), "apbqcr")
        self.assertEqual(s.mergeAlternately(word1 = "ab", word2 = "pqrs"), "apbqrs")
        self.assertEqual(s.mergeAlternately(word1 = "abcd", word2 = "pq"), "apbqcd")
        print("Everything passed")

if __name__ == "__main__":
    unittest.main()