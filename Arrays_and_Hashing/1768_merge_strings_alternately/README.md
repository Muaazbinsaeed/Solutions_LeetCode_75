# Problem: 1768. Merge Strings Alternately (Easy)

**Link:** [Merge Strings Alternately](https://leetcode.com/problems/merge-strings-alternately/)

## 📝 Problem Description

Merge two strings by alternating their characters. If one string is longer, append the remaining characters to the end.

---

### **Examples**

1. **Input:** word1 = "abc", word2 = "pqr"  
   **Output:** "apbqcr"

2. **Input:** word1 = "ab", word2 = "pqrs"  
   **Output:** "apbqrs"

3. **Input:** word1 = "abcd", word2 = "pq"  
   **Output:** "apbqcd"

---

### **Constraints**

- 1 <= word1.length, word2.length <= 100
- `word1` and `word2` consist of lowercase English letters.

---

## 💡 Approach

1. Iterate through both strings simultaneously.
2. Append characters alternately until the shorter string ends.
3. Append the remaining characters of the longer string.

---

### **Complexity Analysis**

- **Time Complexity:** O(n) — Iterate through the longest string.
- **Space Complexity:** O(n) — Result string storage.

---

## 🔍 Tests

- Input: `"abc", "pqr"` → Output: `"apbqcr"`
- Input: `"ab", "pqrs"` → Output: `"apbqrs"`
- Input: `"abcd", "pq"` → Output: `"apbqcd"`






<details> 
    <summary>
        <strong>Click to expand the sample README.md for Problem #1768</strong>
    </summary>

# 1768. Merge Strings Alternately

**Difficulty**: Easy  
**Link**: [LeetCode 1768](https://leetcode.com/problems/merge-strings-alternately/description/)

## Problem Statement

You are given two strings `word1` and `word2`. Merge the strings by adding letters in alternating order, starting with `word1`. If a string is longer than the other, append the additional letters onto the end of the merged string.

### **Examples**

1. **Input:** word1 = "abc", word2 = "pqr"  
   **Output:** "apbqcr"

2. **Input:** word1 = "ab", word2 = "pqrs"  
   **Output:** "apbqrs"

3. **Input:** word1 = "abcd", word2 = "pq"  
   **Output:** "apbqcd"


**Constraints**:
- `1 <= word1.length, word2.length <= 100`
- `word1` and `word2` consist of lowercase English letters.

---

## Approach

1. **Initialization**: Determine the minimum length (`min_len`) of `word1` and `word2`.
2. **Alternate Merge**: For indices `0` to `min_len - 1`, append `word1[i]` and `word2[i]` in order to a result list (or string builder).
3. **Append Remainder**: If one string is longer, append the leftover substring after `min_len` to the result.
4. **Join and Return**: Convert the list of characters to a final string.

### Complexity Analysis
- **Time Complexity**: O(n), where `n` is the combined length of the two strings. We iterate through each character at most once.
- **Space Complexity**: O(n) to store the merged output string.

---

## Files

- [`solution.py`](./solution.py): Contains the `Solution` class with `mergeAlternately` method.
- [`test_solution.py`](./test_solution.py): Contains `unittest` tests to verify correctness.

---

## How to Run

From this directory, execute:
```bash
python -m unittest test_solution.py
```
Or simply:
```bash
python test_solution.py
```

</details>