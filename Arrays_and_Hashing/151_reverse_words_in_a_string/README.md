# 151. Reverse Words in a String

**Difficulty**: Medium  
**Link**: [LeetCode 151](https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=leetcode-75)

---

## Problem Statement

Given an input string `s`, reverse the order of the words.

A **word** is defined as a sequence of **non-space** characters. The words in `s` will be separated by **at least one space**.

Return a string of the words in **reverse order**, concatenated by a **single space**.

Ensure that:
- The returned string has **no leading or trailing spaces**.
- **Multiple spaces** between words are reduced to **a single space**.

---

### **Examples**

1. **Input:**  
   `s = "the sky is blue"`  
   **Output:** `"blue is sky the"`

2. **Input:**  
   `s = "  hello world  "`  
   **Output:** `"world hello"`

3. **Input:**  
   `s = "a good   example"`  
   **Output:** `"example good a"`

---

### **Constraints**

- \(1 \leq \text{s.length} \leq 10^4\)
- `s` contains **English letters**, **digits**, and spaces `' '` (ASCII 32).
- There is **at least one word** in `s`.

---

## **Approach**

### **1. Split, Reverse, and Join (Pythonic)**
- **Logic**:
  - Use Python's built-in `split()` to **remove extra spaces** and **split words**.
  - Reverse the **list of words**.
  - Use `" ".join(words)` to **concatenate words with a single space**.
- **Complexity**:
  - **Time Complexity**: \(O(n)\), since `split()`, `reversed()`, and `join()` all run in **linear time**.
  - **Space Complexity**: \(O(n)\), since we store the words in a list.

---

## **Complexity Analysis**

| Approach                | Time Complexity | Space Complexity |
|-------------------------|----------------|------------------|
| `split() → reverse → join()` | \(O(n)\)  | \(O(n)\) |

---

## **Tests**

### **Basic Cases**
- `"the sky is blue"` → `"blue is sky the"`
- `"  hello world  "` → `"world hello"`
- `"a good   example"` → `"example good a"`

### **Edge Cases**
- `"  multiple   spaces   "` → `"spaces multiple"`
- `"trailing spaces   "` → `"spaces trailing"`
- `"   leading spaces"` → `"spaces leading"`

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
- [`solution.py`](./solution.py): Contains the `Solution` class with the `reverseWords` method.
- [`test_solution.py`](./test_solution.py): Contains `unittest` test cases to validate the solution.

---

This **README** provides a **clear explanation** of the problem, approach, and test cases for **151. Reverse Words in a String**.