# 1071. Greatest Common Divisor of Strings

**Difficulty**: Easy  
**Link**: [LeetCode 1071](https://leetcode.com/problems/greatest-common-divisor-of-strings/description/)

## Problem Statement

For two strings `s` and `t`, we say "`t` divides `s`" if and only if `s = t + t + ... + t` (i.e., `t` is concatenated with itself one or more times).

Given two strings `str1` and `str2`, return the largest string `x` such that `x` divides both `str1` and `str2`.

### Examples

1. **Input:**  
   `str1 = "ABCABC", str2 = "ABC"`  
   **Output:** `"ABC"`

2. **Input:**  
   `str1 = "ABABAB", str2 = "ABAB"`  
   **Output:** `"AB"`

3. **Input:**  
   `str1 = "LEET", str2 = "CODE"`  
   **Output:** `""`

### Constraints

- \(1 \leq \text{str1.length}, \text{str2.length} \leq 1000\)
- `str1` and `str2` consist of uppercase English letters.

---

## Approach

### Solution Algorithm

1. **Iterative GCD by Divisor Checking**:
   - Compute the minimum length of `str1` and `str2`.
   - Iterate from this minimum length down to 1.
   - Check if the current substring divides both strings.

---

### Complexity Analysis

- **Time Complexity**: \(O(n \cdot m)\), where \(n\) and \(m\) are the lengths of `str1` and `str2`. This comes from checking divisors and validating substring repetitions.
- **Space Complexity**: \(O(1)\), as no additional data structures are used.

---

## Tests

### Basic Cases
- Input: `("ABCABC", "ABC")` → Output: `"ABC"`
- Input: `("ABABAB", "ABAB")` → Output: `"AB"`
- Input: `("LEET", "CODE")` → Output: `""`

### Edge Cases
- Input: `("", "ABC")` → Output: `""`
- Input: `("A", "B")` → Output: `""`
- Input: `("A", "A")` → Output: `"A"`

### Large Cases
- Input: `("A" * 1000, "A" * 500)` → Output: `"A" * 500`
- Input: `("AB" * 500, "AB" * 250)` → Output: `"AB" * 250`

---

## Files

- [`solution.py`](./solution.py): Contains the `Solution` class with the `gcdOfStrings` method.
- [`test_solution.py`](./test_solution.py): Contains `unittest` tests to verify correctness.

---

## How to Run

To run the tests:
```bash
python -m unittest test_solution.py
```

Or directly:
```bash
python test_solution.py
``` 

--- 