# 605. Can Place Flowers
### 4_605_can_place_flowers

## Problem: 4  
**Greedy Array Problem (Easy)**  

### **605. Can Place Flowers**

**Link:** [605. Can Place Flowers](https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75)

---

### Problem Description

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.  

Given an integer array `flowerbed` containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer `n`, return `True` if `n` new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule, and `False` otherwise.

---

### Examples

1. **Input:**  
   `flowerbed = [1, 0, 0, 0, 1], n = 1`  
   **Output:** `True`

2. **Input:**  
   `flowerbed = [1, 0, 0, 0, 1], n = 2`  
   **Output:** `False`

3. **Input:**  
   `flowerbed = [0, 0, 1, 0, 0, 0, 1, 0], n = 2`  
   **Output:** `True`

---

### Constraints

- \(1 \leq \text{flowerbed.length} \leq 2 \times 10^4\)
- \(0 \leq n \leq \text{flowerbed.length}\)
- `flowerbed[i]` is `0` or `1`.
- There are no two adjacent flowers in `flowerbed`.

---

### Approach

#### **Solution 1: Space Complexity O(n)**

- **Logic**:
  1. Add padding (`0`s) at both ends of the flowerbed to simplify edge handling.
  2. Iterate through the flowerbed and check if a flower can be planted at the current position (`flowerbed[i-1:i+2]` contains no `1`).
  3. If a flower is planted, decrement `n`.
  4. If `n` becomes `0`, return `True`.
- **Complexity**:
  - Time Complexity: \(O(n)\), where \(n\) is the length of the flowerbed.
  - Space Complexity: \(O(n)\), due to the padded flowerbed.

#### **Solution 2: Space Complexity O(1)**

- **Logic**:
  1. Handle small flowerbeds explicitly (\( \text{len} < 3 \)).
  2. Check and plant at the first and last positions separately.
  3. Iterate through the middle positions, planting flowers where possible.
  4. Decrement `n` for every flower planted and stop early if `n` becomes `0`.
- **Complexity**:
  - Time Complexity: \(O(n)\), where \(n\) is the length of the flowerbed.
  - Space Complexity: \(O(1)\), since no additional memory is used.

---

### Complexity Analysis

| Approach               | Time Complexity | Space Complexity |
|------------------------|-----------------|------------------|
| Solution 1 (Padding)   | \(O(n)\)        | \(O(n)\)         |
| Solution 2 (In-place)  | \(O(n)\)        | \(O(1)\)         |

---

### Tests

#### Basic Cases
- `flowerbed = [1, 0, 0, 0, 1], n = 1` → `True`
- `flowerbed = [1, 0, 0, 0, 1], n = 2` → `False`

#### Edge Cases
- `flowerbed = [1], n = 0` → `True`
- `flowerbed = [0], n = 1` → `True`
- `flowerbed = [0, 0, 0], n = 2` → `True`
- `flowerbed = [0, 0, 0], n = 3` → `False`

#### Large Cases
- `flowerbed = [0] * 10**4, n = 10**3` → `True`
- `flowerbed = [1] + [0] * 10**4 + [1], n = 500` → `True`

---

### How to Run

1. Run the **Solution** with quick manual checks:
   ```bash
   python solution.py
   ```

2. Run the **Tests**:
   ```bash
   python -m unittest test_solution.py
   ```

---

### Files

- [`solution.py`](./solution.py): Contains the `Solution` class with both implementations.
- [`test_solution.py`](./test_solution.py): Contains `unittest` test cases to validate the solution.

--- 

This README provides a comprehensive understanding of the problem, approach, and implementation details for **605. Can Place Flowers**.

