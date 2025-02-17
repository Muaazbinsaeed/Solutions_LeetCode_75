# 3_1431_kids_with_the_greatest_number_of_candies

# ## Problem: 3
# Array / String Merge Strings Alternately (Easy)

# # 1431. Kids With the Greatest Number of Candies
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/?envType=study-plan-v2&envId=leetcode-75

# There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

# Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

# Note that multiple kids can have the greatest number of candies.

 

# Example 1:

# Input: candies = [2,3,5,1,3], extraCandies = 3
# Output: [true,true,true,false,true] 
# Explanation: If you give all extraCandies to:
# - Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
# - Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
# - Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
# - Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
# - Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
# Example 2:

# Input: candies = [4,2,1,1,2], extraCandies = 1
# Output: [true,false,false,false,false] 
# Explanation: There is only 1 extra candy.
# Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.
# Example 3:

# Input: candies = [12,1,12], extraCandies = 10
# Output: [true,false,true]
 

# Constraints:

# n == candies.length
# 2 <= n <= 100
# 1 <= candies[i] <= 100
# 1 <= extraCandies <= 50

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
       # Find the maximum number of candies among all kids
        max_candy = max(candies)
        
        # Return a boolean list where each element indicates if the current
        # kid can have the greatest number of candies after adding extraCandies
        return [ True if ((max_candy - (x + extraCandies)) <= 0) else False for x in candies ]


if __name__ == "__main__":
    # Quick manual checks
    s = Solution()
    print(s.kidsWithCandies([2, 3, 5, 1, 3], 3))  # Output: [True, True, True, False, True]
    print(s.kidsWithCandies([4, 2, 1, 1, 2], 1))  # Output: [True, False, False, False, False]
    print(s.kidsWithCandies([12, 1, 12], 10))    # Output: [True, False, True]
