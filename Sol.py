#1_1768_MergeStringsAlternately

# ## Problem: 1
# Array / String
# Merge Strings Alternately
# (Easy)

# # 1768. Merge Strings Alternately
# https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75

# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

 
# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
# Example 2:

# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s
# Example 3:

# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d
 
# Constraints:

# 1 <= word1.length, word2.length <= 100
# word1 and word2 consist of lowercase English letters.


class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
    
        len_1 = len(word1)
        len_2 = len(word2)
        min_len = min (len_1, len_2)
        big_word = ""
        for i in range(min_len):
            big_word += word1[i]
            big_word += word2[i]

        if len_1 > min_len:
            big_word += word1[min_len:]
        else:
            big_word += word2[min_len:]
        return big_word
    

# Input: word1 = "abc", word2 = "pqr" Output: "apbqcr"
# Input: word1 = "ab", word2 = "pqrs" Output: "apbqrs" 
# Input: word1 = "abcd", word2 = "pq" Output: "apbqcd"


if __name__ == "__main__":
    s = Solution()

    print (s.mergeAlternately(word1 = "abc", word2 = "pqr"))
    print (s.mergeAlternately(word1 = "ab", word2 = "pqrs"))
    print (s.mergeAlternately(word1 = "abcd", word2 = "pq"))

    assert s.mergeAlternately(word1 = "abc", word2 = "pqr") == "apbqcr", "Should be apbqcr"
    assert s.mergeAlternately(word1 = "ab", word2 = "pqrs") == "apbqrs", "Should be apbqrs"
    assert s.mergeAlternately(word1 = "abcd", word2 = "pq") == "apbqcd", "Should be apbqcd"
    
    print("Everything passed")

