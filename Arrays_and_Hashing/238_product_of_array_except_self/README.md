# 238. Product of Array Except Self

**Difficulty**: Medium  
**Link**: [LeetCode 238](https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=leetcode-75)

---

## Problem Statement

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the **product of all elements of `nums` except `nums[i]`**.

The product of any prefix or suffix of `nums` is **guaranteed to fit in a 32-bit integer**.

You **must** solve the problem **without using the division operation** and in **O(n) time complexity**.

---

### **Examples**

1. **Input:**  
   `nums = [1, 2, 3, 4]`  
   **Output:** `[24, 12, 8, 6]`

2. **Input:**  
   `nums = [-1, 1, 0, -3, 3]`  
   **Output:** `[0, 0, 9, 0, 0]`

---

### **Constraints**

- \(2 \leq \text{nums.length} \leq 10^5\)
- \(-30 \leq \text{nums[i]} \leq 30\)
- The **product** of any prefix or suffix of `nums` fits in a **32-bit integer**.

---

## **Approach**

### **1. Prefix and Suffix Product**
- **Logic**:
  - Use **two passes**:  
    1. Compute **prefix product** from left to right.
    2. Compute **suffix product** from right to left and update results.
  - This ensures **O(n) time complexity** while avoiding division.
- **Complexity**:
  - **Time Complexity**: \(O(n)\), as we iterate through the array twice.
  - **Space Complexity**: \(O(1)\), since we use the output array itself for storing results.

---

## **Complexity Analysis**

| Approach        | Time Complexity | Space Complexity |
|----------------|----------------|------------------|
| Prefix & Suffix Product | \(O(n)\) | \(O(1)\) |

---

## **Tests**

### **Basic Cases**
- `[1, 2, 3, 4]` → `[24, 12, 8, 6]`
- `[-1, 1, 0, -3, 3]` → `[0, 0, 9, 0, 0]`

### **Edge Cases**
- `[0, 0]` → `[0, 0]`
- `[1]` → `[1]`
- `[-1, -1]` → `[-1, -1]`

### **Performance Cases**
- **Large Input**: `[1] * 10^5` → `[1] * 10^5`

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
- [`solution.py`](./solution.py): Contains the `Solution` class with the `productExceptSelf` method.
- [`test_solution.py`](./test_solution.py): Contains `unittest` test cases to validate the solution.

---

## **Explanation of Prefix & Suffix Products**
| **Index** | **Nums** | **Prefix Product** | **Suffix Product** | **Final Result** |
|-----------|---------|--------------------|--------------------|------------------|
| `0`       | `1`     | `1`                | `24`               | `24` |
| `1`       | `2`     | `1`                | `12`               | `12`  |
| `2`       | `3`     | `2`                | `4`                | `8`  |
| `3`       | `4`     | `6`                | `1`                | `6`  |

**Final Output:**
```python
[24, 12, 8, 6]
```

---

This **README** provides a **clear explanation** of the problem, approach, and test cases for **238. Product of Array Except Self**.



# Detailed Explanation:

### **Breaking Down Prefix & Suffix Calculation (ELI5)**

The core idea of the **Product of Array Except Self** problem is to compute the **product of all numbers except the current one** **without using division**.

To achieve this, we use **two passes**:
1. **Prefix Product**: Stores the product of all elements **before** the current index.
2. **Suffix Product**: Stores the product of all elements **after** the current index.

---

## **Example**
### **Input**
```python
nums = [3, 2, 5, 4]
```

### **Step 1: Compute Prefix Products**
- **Each `prefix[i]` stores the product of all elements before `nums[i]`**.
- We initialize `prefix[0] = 1` (since there are no elements before index `0`).

| **Index `i`** | **nums[i]** | **Prefix Product (before `nums[i]`)** | **Why?** |
|--------------|------------|--------------------------------|-------|
| `0`          | `3`        | `1`                            | No elements before `3` |
| `1`          | `2`        | `3`                            | `1 * 3 = 3` |
| `2`          | `5`        | `3 * 2 = 6`                    | `3 * 2 = 6` |
| `3`          | `4`        | `6 * 5 = 30`                   | `3 * 2 * 5 = 30` |

### **Prefix Array**
```
prefix = [ 1,  3,  6, 30 ]
```

---

### **Step 2: Compute Suffix Products**
- **Each `suffix[i]` stores the product of all elements after `nums[i]`**.
- We initialize `suffix[n-1] = 1` (since there are no elements after the last index).

| **Index `i`** | **nums[i]** | **Suffix Product (after `nums[i]`)** | **Why?** |
|--------------|------------|--------------------------------|-------|
| `3`          | `4`        | `1`                            | No elements after `4` |
| `2`          | `5`        | `4 * 1 = 4`                    | `4` |
| `1`          | `2`        | `5 * 4 = 20`                   | `5 * 4` |
| `0`          | `3`        | `2 * 20 = 40`                  | `2 * 5 * 4` |

### **Suffix Array**
```
suffix = [ 40,  20,  4,  1 ]
```

---

### **Step 3: Multiply Prefix and Suffix**
Now, the final **result array** is calculated as:
```python
result[i] = prefix[i] * suffix[i]
```

| **Index `i`** | **Prefix[i]** | **Suffix[i]** | **Result[i] = Prefix[i] * Suffix[i]** |
|--------------|--------------|--------------|----------------------------------|
| `0`          | `1`          | `40`         | `1 * 40 = 40`  |
| `1`          | `3`          | `20`         | `3 * 20 = 60`  |
| `2`          | `6`          | `4`          | `6 * 4 = 24`   |
| `3`          | `30`         | `1`          | `30 * 1 = 30`  |

### **Final Output**
```
result = [40, 60, 24, 30]
```

---

### **Visualizing Prefix & Suffix Products**
#### **Step-by-Step Calculation for Each Index**
Let's look at the calculations for **each index**:

1. **For `nums[0] = 3`**:
   - Prefix: `1`
   - Suffix: `2 × 5 × 4 = 40`
   - **Final Value**: `1 × 40 = 40`

2. **For `nums[1] = 2`**:
   - Prefix: `3`
   - Suffix: `5 × 4 = 20`
   - **Final Value**: `3 × 20 = 60`

3. **For `nums[2] = 5`**:
   - Prefix: `3 × 2 = 6`
   - Suffix: `4`
   - **Final Value**: `6 × 4 = 24`

4. **For `nums[3] = 4`**:
   - Prefix: `3 × 2 × 5 = 30`
   - Suffix: `1`
   - **Final Value**: `30 × 1 = 30`

---

## **Key Observations**
1. **Prefix at index `i`** stores **the product of elements before `nums[i]`**.
2. **Suffix at index `i`** stores **the product of elements after `nums[i]`**.
3. **Multiplying both gives the desired result**:  
   `result[i] = prefix[i] * suffix[i]`
4. **Efficient Calculation**:
   - We use **two passes** (left-to-right and right-to-left).
   - We **avoid using division**.
   - **Time Complexity = O(n)**.
   - **Space Complexity = O(1)** (excluding result array).

---

## **Complexity Analysis**
| **Operation** | **Time Complexity** | **Space Complexity** |
|--------------|---------------------|---------------------|
| Compute Prefix Products | \(O(n)\) | \(O(1)\) |
| Compute Suffix Products | \(O(n)\) | \(O(1)\) |
| **Total Complexity** | **\(O(n)\)** | **\(O(1)\)** |

This is **one of the most optimized approaches** to solve the problem! 🚀