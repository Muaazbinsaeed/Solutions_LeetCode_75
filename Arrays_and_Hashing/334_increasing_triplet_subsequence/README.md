# 334. Increasing Triplet Subsequence

**Difficulty**: Medium  
**Link**: [LeetCode 334](https://leetcode.com/problems/increasing-triplet-subsequence/description/?envType=study-plan-v2&envId=leetcode-75)

---

## **Problem Statement**

Given an integer array `nums`, return `True` if there exists a triple of indices `(i, j, k)` such that:

- \( i < j < k \)
- \( nums[i] < nums[j] < nums[k] \)

If no such indices exist, return `False`.

---

### **Examples**

#### **Example 1**
**Input:**  
`nums = [1, 2, 3, 4, 5]`  
**Output:** `True`  
**Explanation:** Any sequence of three increasing numbers works.

#### **Example 2**
**Input:**  
`nums = [5, 4, 3, 2, 1]`  
**Output:** `False`  
**Explanation:** No increasing triplet subsequence exists.

#### **Example 3**
**Input:**  
`nums = [2, 1, 5, 0, 4, 6]`  
**Output:** `True`  
**Explanation:** The increasing sequence is `[0, 4, 6]`.

---

## **Constraints**

- \(1 \leq \text{nums.length} \leq 5 \times 10^5\)
- \(-2^{31} \leq \text{nums[i]} \leq 2^{31} - 1\)

---

## **Approach**

### **1. Greedy Two-Variable Approach**
- **Logic**:
  - Keep track of two smallest numbers: `first` and `second`.
  - Iterate through the array:
    - If `num <= first`, update `first`.
    - Else if `num <= second`, update `second`.
    - Else, return `True` (as we found `first < second < num`).
- **Complexity**:
  - **Time Complexity**: \(O(n)\), since we iterate once.
  - **Space Complexity**: \(O(1)\), as we use only two variables.

---

## **Complexity Analysis**

| Approach        | Time Complexity | Space Complexity |
|----------------|----------------|------------------|
| Greedy Two-Variable | \(O(n)\) | \(O(1)\) |

---

## **Tests**

### **Basic Cases**
- `[1, 2, 3, 4, 5]` → `True`
- `[5, 4, 3, 2, 1]` → `False`
- `[2, 1, 5, 0, 4, 6]` → `True`

### **Edge Cases**
- `[1, 1, 1, 1, 1]` → `False`
- `[20, 100, 10, 12, 5, 13]` → `True`
- `[2, 3, 2, 3, 2, 3, 4]` → `True`

### **Performance Cases**
- **Large Input**: `list(range(10^5))` → `True`

---

## **How to Run**

1. Run the **Solution** with manual checks:
   ```bash
   python solution.py
   ```

2. Run the **Tests**:
   ```bash
   python -m unittest test_solution.py
   ```

---

## **Files**
- [`solution.py`](./solution.py): Contains the `Solution` class with the `increasingTriplet` method.
- [`test_solution.py`](./test_solution.py): Contains `unittest` test cases to validate the solution.

---

## **Why This Works?**
1. **Tracks Two Smallest Values (`first` and `second`)**:
   - If a third number is found that is greater than both, we return `True`.
2. **Efficient O(n) Time Complexity**:
   - Only **one pass** is needed, keeping it optimal for large inputs.
3. **Uses O(1) Extra Space**:
   - We only maintain two variables.

This approach **efficiently solves the problem** without extra space or nested loops. 🚀