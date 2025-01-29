# 5_345_reverse_vowels_of_a_string

# ## Problem: 5
# Two Pointer / String Problem (Easy)

# # 345. Reverse Vowels of a String
# https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=study-plan-v2&envId=leetcode-75

# 345. Reverse Vowels of a String
# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# Example 1:
# Input: s = "IceCreAm"
# Output: "AceCreIm"

# Explanation:
# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"

# Constraints:
# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Define a set of vowels (both uppercase and lowercase)
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        s_arr = list(s)  # Convert string to a list for mutability
        i, j = 0, len(s_arr) - 1  # Initialize two pointers

        while i < j:
            # Move left pointer until it finds a vowel
            while i < j and s_arr[i] not in vowels: 
                i += 1
                
            # Move right pointer until it finds a vowel
            while i < j and s_arr[j] not in vowels:  
                j -= 1

            # Swap the vowels
            s_arr[i], s_arr[j] = s_arr[j], s_arr[i]
            i += 1
            j -= 1

        return "".join(s_arr)  # Convert list back to a string  
    
if __name__ == "__main__":
    # Quick manual checks
    s = Solution()
    print(s.reverseVowels("IceCreAm"))  # Output: "AceCreIm"
    print(s.reverseVowels("leetcode"))  # Output: "leotcede"
    print("Everything passed!")
