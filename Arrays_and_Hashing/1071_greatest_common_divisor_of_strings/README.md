# 1071. Greatest Common Divisor of Strings

**Difficulty**: Easy  
**Link**: [LeetCode 1071](https://leetcode.com/problems/greatest-common-divisor-of-strings/description/)

---

## Problem Statement

For two strings `str1` and `str2`, we say "t divides s" if and only if `s = t + t + ... + t` (i.e., `t` is concatenated with itself one or more times).

Given two strings `str1` and `str2`, return the largest string `x` such that `x` divides both `str1` and `str2`.

---

### **Examples**

1. **Input:** str1 = "ABCABC", str2 = "ABC"  
   **Output:** `"ABC"`

2. **Input:** str1 = "ABABAB", str2 = "ABAB"  
   **Output:** `"AB"`

3. **Input:** str1 = "LEET", str2 = "CODE"  
   **Output:** `""`

---

### **Constraints**

- `1 <= str1.length, str2.length <= 1000`
- `str1` and `str2` consist of uppercase English letters.

---

## Approach

### **1. String Properties and GCD**
- Check if `str1 + str2 == str2 + str1`. If not, return `""` since no common divisor exists.
- Find the GCD of the lengths of `str1` and `str2`.
- Return the prefix of `str1` with a length equal to the GCD.

---

### Complexity Analysis

- **Time Complexity**: \(O(N + M)\), where \(N\) and \(M\) are the lengths of `str1` and `str2`.
- **Space Complexity**: \(O(1)\).

---

## Files

- [`solution.py`](./solution.py): Contains the `Solution` class with the `gcdOfStrings` method.
- [`test_solution.py`](./test_solution.py): Contains `unittest` tests to verify correctness.

---

## How to Run

1. Clone the repository or navigate to the directory containing the solution files.
2. Execute the tests:
   ```bash
   python -m unittest test_solution.py
   ```
   Or simply:
   ```bash
   python test_solution.py
   ```

---

## Example Test Cases

- **Input:** `"ABCABC", "ABC"` → **Output:** `"ABC"`
- **Input:** `"ABABAB", "ABAB"` → **Output:** `"AB"`
- **Input:** `"LEET", "CODE"` → **Output:** `""`

---

## Additional Notes

This solution uses mathematical GCD to determine the largest common divisor substring efficiently. It leverages the associative property of concatenation to quickly check if a divisor exists.