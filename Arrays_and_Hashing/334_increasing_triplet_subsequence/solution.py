# 8_334_increasing_triplet_subsequence

# ## Problem: 8
# Array / Greedy (Medium)

# # 334. Increasing Triplet Subsequence
# https://leetcode.com/problems/increasing-triplet-subsequence/description/?envType=study-plan-v2&envId=leetcode-75

# Given an integer array nums, return true if there exists a triple of indices (i, j, k) 
# such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exist, return false.

# Example 1:
# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any sequence of three increasing numbers works.

# Example 2:
# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No increasing triplet subsequence exists.

# Constraints:
# - 1 <= nums.length <= 5 * 10^5
# - -2^31 <= nums[i] <= 2^31 - 1

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first_num = second_num = float('inf')
        for num in nums:
            if num <= first_num:
                first_num = num  # number should be first_num
            elif num <= second_num:
                second_num = num  # second smallest number should be second_num
            else:
                return True  #triplet found: first_num < second_num < num
        
        return False

if __name__ == "__main__":
    # Quick manual checks
    s = Solution()
    print(s.increasingTriplet([1,2,3,4,5]))  # Output: True
    print(s.increasingTriplet([5,4,3,2,1]))  # Output: False
    print(s.increasingTriplet([2,1,5,0,4,6]))  # Output: True
    print("Everything passed!")
