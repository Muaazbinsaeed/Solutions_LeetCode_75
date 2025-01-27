# 2_1071_GreatestCommonDivisorOfStrings

# ## Problem: 2
# Array / String Merge Strings Alternately (Easy)

# # 1071. Greatest Common Divisor of Strings
# https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=study-plan-v2&envId=leetcode-75

# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.


# Example 1:
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"

# Example 2:
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"

# Example 3:
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
 

# Constraints:

# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of English uppercase letters.

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        
        len_1, len_2 = len(str1), len(str2)
        min_len = min(len_1, len_2)
#         word = ""
        
        for i in range(min_len, 0 , -1):  # Start with the maximum possible length
            if (len_1 % i == 0) and (len_2 % i == 0):  # Check divisibility
                word = str1[:i]
                if (word * (len_1 // i) == str1) and (word * (len_2 // i) == str2):
                    return word
            
        return ""

# Example 1: Input: str1 = "ABCABC", str2 = "ABC" Output: "ABC"
# Example 2: Input: str1 = "ABABAB", str2 = "ABAB" Output: "AB"
# Example 3: Input: str1 = "LEET", str2 = "CODE" Output: ""


if __name__ == "__main__":
    # Optional: Some quick manual checks before running the tests
    s = Solution()

    result1 = s.gcdOfStrings("ABCABC", "ABC")
    print("Input: word1='ABCABC', word2='ABC' -->", result1)
    assert result1 == "ABC"

    result2 = s.gcdOfStrings("ABABAB", "ABAB")
    print("Input: word1='ABABAB', word2='ABAB' -->", result2)
    assert result2 == "AB"

    result3 = s.gcdOfStrings("LEET", "CODE")
    print("Input: word1='LEET', word2='CODE' -->", result3)
    assert result3 == ""

    print("Everything passed!")
