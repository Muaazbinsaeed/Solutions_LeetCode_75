import unittest
from solution import Solution

class TestCanPlaceFlowers(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_basic_cases(self):
        self.assertTrue(self.s.canPlaceFlowers([1, 0, 0, 0, 1], 1))
        self.assertFalse(self.s.canPlaceFlowers([1, 0, 0, 0, 1], 2))
        self.assertTrue(self.s.canPlaceFlowers([0, 0, 1, 0, 0, 0, 1, 0], 2))

    def test_single_element(self):
        # Single element flowerbed
        self.assertTrue(self.s.canPlaceFlowers([1], 0))  # No new flowers needed
        self.assertFalse(self.s.canPlaceFlowers([1], 1))  # Can't plant in a filled slot
        self.assertTrue(self.s.canPlaceFlowers([0], 0))  # No new flowers needed
        self.assertTrue(self.s.canPlaceFlowers([0], 1))  # Can plant in an empty slot

    def test_small_flowerbeds(self):
        # Basic cases with small flowerbeds
        self.assertTrue(self.s.canPlaceFlowers([1, 0, 0, 0, 1], 1))  # Plant in the middle
        self.assertFalse(self.s.canPlaceFlowers([1, 0, 0, 0, 1], 2))  # Only one spot available
        self.assertTrue(self.s.canPlaceFlowers([0, 0, 1, 0, 0, 0, 1, 0], 2))  # Two spots available

    def test_edge_placements(self):
        # Planting at edges
        self.assertTrue(self.s.canPlaceFlowers([0, 0, 1], 1))  # Can plant at the beginning
        self.assertFalse(self.s.canPlaceFlowers([0, 1, 0], 1))  # No valid spots
        self.assertTrue(self.s.canPlaceFlowers([1, 0, 0], 1))  # Can plant at the end
        self.assertTrue(self.s.canPlaceFlowers([0, 0, 0], 1))  # One flower can be planted
        self.assertTrue(self.s.canPlaceFlowers([0, 0, 0], 2))  # Two flowers can be planted
        self.assertFalse(self.s.canPlaceFlowers([1, 1, 1], 1))  
        self.assertFalse(self.s.canPlaceFlowers([0, 0, 0], 3))  

    def test_large_flowerbeds(self):
        # Larger flowerbeds
        self.assertTrue(self.s.canPlaceFlowers([1, 0, 0, 0, 0, 0, 1], 2))  # Two spots available
        self.assertFalse(self.s.canPlaceFlowers([1, 0, 0, 0, 0, 0, 1], 3))  # Only two spots available

        # Large input test
        flowerbed = [0] * 1000
        self.assertTrue(self.s.canPlaceFlowers(flowerbed, 500))
        self.assertFalse(self.s.canPlaceFlowers(flowerbed, 502))


    def test_no_planting_needed(self):
        # Cases where no new flowers are needed
        self.assertTrue(self.s.canPlaceFlowers([1, 0, 0, 1], 0))  # Already meets requirement
        self.assertTrue(self.s.canPlaceFlowers([0, 0, 0, 0, 0], 0))  # No new flowers needed

    def test_full_flowerbeds(self):
        # Completely filled flowerbed
        self.assertFalse(self.s.canPlaceFlowers([1, 1, 1, 1, 1], 1))  # No space to plant
        self.assertFalse(self.s.canPlaceFlowers([1, 1, 1, 1], 1))  # No space to plant

    def test_all_empty(self):
        # Case where the flowerbed is entirely empty
        self.assertTrue(self.s.canPlaceFlowers([0, 0, 0, 0, 0], 2))
        self.assertTrue(self.s.canPlaceFlowers([0, 0, 0, 0, 0], 3))
        self.assertFalse(self.s.canPlaceFlowers([0, 0, 0, 0, 0], 4))

if __name__ == "__main__":
    unittest.main()
