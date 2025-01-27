# 1431. Kids With the Greatest Number of Candies

**Difficulty**: Easy  
**Link**: [LeetCode 1431](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/)

## Problem Statement

You are given an integer array `candies`, where each `candies[i]` represents the number of candies the \(i^{th}\) kid has, and an integer `extraCandies`, denoting the number of extra candies you can give to any kid.

Return a boolean array `result` of length `candies.length`, where `result[i]` is `True` if, after giving the \(i^{th}\) kid all the `extraCandies`, they have the greatest number of candies among all the kids.

### Examples

1. **Input:**  
   `candies = [2, 3, 5, 1, 3], extraCandies = 3`  
   **Output:** `[True, True, True, False, True]`

2. **Input:**  
   `candies = [4, 2, 1, 1, 2], extraCandies = 1`  
   **Output:** `[True, False, False, False, False]`

3. **Input:**  
   `candies = [12, 1, 12], extraCandies = 10`  
   **Output:** `[True, False, True]`

---

## Constraints

- \(2 \leq \text{candies.length} \leq 100\)
- \(1 \leq \text{candies[i]} \leq 100\)
- \(1 \leq \text{extraCandies} \leq 50\)

---

## Approach

1. **Find the Maximum Candies**:
   - Determine the maximum number of candies any kid currently has.

2. **Calculate Boolean Array**:
   - For each kid, check if their candies, when added with `extraCandies`, are greater than or equal to the maximum candies.

3. **Return the Result**:
   - Construct and return the boolean array.

---

### Complexity Analysis

- **Time Complexity**: \(O(n)\), where \(n\) is the length of the `candies` array. We iterate through the array twice: once to find the maximum and once to construct the result array.
- **Space Complexity**: \(O(n)\), where \(n\) is the length of the output array.

---

## Files

- [`solution.py`](./solution.py): Contains the `Solution` class with the `kidsWithCandies` method.
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