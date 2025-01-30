# 7_238_product_of_array_except_self

# ## Problem: 7
# Array Manipulation / Prefix Product (Medium)

# # 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=leetcode-75

# Given an integer array nums, return an array answer such that answer[i] is equal to 
# the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [1] * n  # Initialize result array with all 1s
        
        # Compute prefix products
        prefix = 1
        for i in range(n):
            result[i] = prefix  # Store the product of all elements before nums[i]
            prefix *= nums[i]  # Update prefix

        # Compute suffix products and update result array
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix  # Multiply the suffix product
            suffix *= nums[i]  # Update suffix
        
        return result


if __name__ == "__main__":
    # Quick manual checks
    s = Solution()
    print(s.productExceptSelf([1, 2, 3, 4]))  # Output: [24, 12, 8, 6]
    print(s.productExceptSelf([-1, 1, 0, -3, 3]))  # Output: [0, 0, 9, 0, 0]
    print("Everything passed!")
