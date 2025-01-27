# # 4_605_can_place_flowers

# # ## Problem: 4
# # Greedy Array Problem (Easy)

# # # 605. Can Place Flowers

# https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75

# 605. Can Place Flowers

# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

# Example 1:

# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
# Example 2:

# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false
 
# Constraints:

# 1 <= flowerbed.length <= 2 * 104
# flowerbed[i] is 0 or 1.
# There are no two adjacent flowers in flowerbed.
# 0 <= n <= flowerbed.length

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        # Solution 1
        # Space Complexity O(n) due to padding

        if n<1:
            return True
        
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
                
            # Checking if the current plot and its neighbors are empty
            if 1 not in flowerbed[i-1:i+2]:
                flowerbed[i] = 1  # Plant a flower
                n -= 1
                if n<1:
                    return True
        
        return False
    

        # # Solution 2
        # # Space Complexity (1)
        # len_flowerbed = len(flowerbed)

        # # If no flowers need to be planted, return True immediately
        # if n==0:
        #     return True

        # #n > 0 &  2 len
        # if len_flowerbed < 3:
        #     if 1 not in flowerbed and n==1:
        #         return True
        #     else:
        #         return False

        # # Check and plant at the first position if possible
        # if 1 not in flowerbed[:2]:
        #     flowerbed[0] = 1
        #     n -= 1
        #     if n == 0:
        #         return True
      
        # # Check and plant at the last position if possible
        # if 1 not in flowerbed[len_flowerbed-2:]:
        #     flowerbed[len_flowerbed-1] = 1
        #     n -= 1
        #     if n == 0:
        #         return True

        #  # Check and plant in the middle positions
        # for i in range(1, len_flowerbed-1):
        #     # If the current position and its neighbors are empty, plant a flower
        #     if 1 not in flowerbed[i-1:i+1]:
        #         flowerbed[i] = 1
        #         n -= 1
        #         if n == 0:
        #             return True
                    
        # return False



if __name__ == "__main__":
    # Quick manual checks
    s = Solution()
    print(s.canPlaceFlowers([1, 0, 0, 0, 1], 1))  # Output: True
    print(s.canPlaceFlowers([1, 0, 0, 0, 1], 2))  # Output: False
    print(s.canPlaceFlowers([0, 0, 1, 0, 0, 0, 1, 0], 2))  # Output: True

    print("Everything passed!")
