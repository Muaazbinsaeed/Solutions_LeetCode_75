# 345. Reverse Vowels of a String

**Difficulty**: Easy  
**Link**: [LeetCode 345](https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=study-plan-v2&envId=leetcode-75)

---

## Problem Statement

Given a string `s`, reverse only all the vowels in the string and return it.
The vowels are `'a', 'e', 'i', 'o', 'u'`, and they can appear in both **lowercase and uppercase**.

---

### **Examples**

1. **Input:**  
   `s = "hello"`  
   **Output:** `"holle"`

2. **Input:**  
   `s = "leetcode"`  
   **Output:** `"leotcede"`

3. **Input:**  
   `s = "aA"`  
   **Output:** `"Aa"`

---

### **Constraints**

- \(1 \leq \text{s.length} \leq 3 \times 10^5\)
- `s` consists of **printable ASCII** characters.

---

## **Approach**

### **1. Two-Pointer Technique**
- **Logic**:
  - Use **two pointers** (`left` at start, `right` at end).
  - Move `left` forward until a vowel is found.
  - Move `right` backward until a vowel is found.
  - Swap them and repeat.
- **Complexity**:
  - **Time Complexity**: \(O(n)\), since each character is checked once.
  - **Space Complexity**: \(O(n)\), since strings are immutable, and a list conversion is needed.

---

## **Complexity Analysis**

| Approach      | Time Complexity | Space Complexity |
|--------------|-----------------|------------------|
| Two-Pointer  | \(O(n)\)        | \(O(n)\)        |

---

## **Tests**

### **Basic Cases**
- `"hello"` → `"holle"`
- `"leetcode"` → `"leotcede"`

### **Edge Cases**
- `"aA"` → `"Aa"`
- `"aeiou"` → `"uoiea"`
- `"AEIOU"` → `"UOIEA"`

### **Performance Cases**
- `"a" * 10^5 + "e"` → `"e" + "a" * 10^5`

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
- [`solution.py`](./solution.py): Contains the `Solution` class with the `reverseVowels` method.
- [`test_solution.py`](./test_solution.py): Contains `unittest` test cases to validate the solution.

---

This README provides a **clear explanation** of the problem, solution, and test cases for **345. Reverse Vowels of a String**.
```