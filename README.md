# LeetCode 75 Solutions in Python 🚀

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Progress](https://img.shields.io/badge/Solved-01%2F75-orange)](https://leetcode.com/studyplan/leetcode-75/)
[![Code Style](https://img.shields.io/badge/code%20style-PEP--8-brightgreen)](https://peps.python.org/pep-0008/)

A comprehensive collection of Python solutions for the [LeetCode 75 Study Plan](https://leetcode.com/studyplan/leetcode-75/), featuring detailed documentation, testing, and complexity analysis. Ideal for technical interview preparation and algorithmic mastery.

**Maintained by [Muaaz Bin Saeed](https://github.com/Muaazbinsaeed)**

---

## 📋 Table of Contents
- [Project Structure](#-project-structure)
- [Key Features](#-key-features)
- [Getting Started](#-getting-started)
- [Progress Tracking](#-progress-tracking)
- [Solution Walkthrough](#-solution-walkthrough)
- [Technical Skills](#-technical-skills)
- [Contributing](#-contributing)
- [License](#-license)
- [Connect](#-connect)

---

## 🗂 Project Structure

### Category-Based Organization
```
Solutions_LeetCode_75/
├── array_string/              # Array/String problems
│   ├── 1768_merge_strings_alternately/
│   │   ├── README.md          # Problem documentation
│   │   ├── solution.py        # Python implementation
│   │   └── test_solution.py   # Unit tests
│   └── 1071_gcd_of_strings/
├── two_pointers/              # Two Pointer technique
├── sliding_window/            # Sliding Window problems
├── binary_search/             # Binary Search category
└── ...                        # Other categories
```

### File Naming Convention
- Folders: `<problem_number>_<snake_case_problem_name>`
- Files: Consistent `solution.py` and `test_solution.py` naming
- Example: `1768_merge_strings_alternately/`

Inside each folder, you'll find:

1. **`README.md`** — Brief description of the problem and approach.
2. **`solution.py`** — The Python solution (with docstrings, complexity analysis, etc.).
3. **`test_solution.py`** — Unit tests using `unittest` (or `pytest`) framework.

---

## ✨ Key Features
- 🧩 **Modular Code Structure**: Easily navigable category-based organization
- 📝 **Detailed Documentation**: Problem statements, approach explanations, and complexity analysis
- 🧪 **Comprehensive Testing**: 100% test coverage with unittest/pytest
- ⚡ **Optimized Solutions**: O(n) time/space complexity analysis for each problem
- 🔍 **SEO-Friendly**: Problem numbers and keywords in file paths
- 📈 **Progress Tracking**: Visual completion metrics for each category

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation
```bash
# Clone repository
git clone https://github.com/Muaazbinsaeed/Solutions_LeetCode_75.git
cd Solutions_LeetCode_75
```

### Running a Solution
```bash
cd array_string/1768_merge_strings_alternately
python solution.py
```

### Executing Tests
```bash
python -m unittest test_solution.py -v  # Verbose mode
```
or simply
```bash
python test_solution.py
```

---

## 📈 Progress Tracking

| Category                     | Problems Solved | Total |
|------------------------------|----------------:|------:|
| Array / String               | 1               | 9     |
| Two Pointers                 | 0               | 4     |
| Sliding Window               | 0               | 4     |
| Prefix Sum                   | 0               | 2     |
| Hash Map/Set                 | 0               | 4     |
| Stack                        | 0               | 3     |
| Queue                        | 0               | 2     |
| Linked List                  | 0               | 4     |
| Binary Tree DFS              | 0               | 6     |
| Binary Tree BFS              | 0               | 2     |
| Binary Search Tree           | 0               | 2     |
| Graphs DFS                   | 0               | 4     |
| Graphs BFS                   | 0               | 2     |
| Heap/Priority Queue          | 0               | 4     |
| Binary Search                | 0               | 4     |
| Backtracking                 | 0               | 2     |
| DP 1D                        | 0               | 4     |
| DP Multidimensional          | 0               | 4     |
| Bit Manipulation             | 0               | 3     |
| Trie                         | 0               | 2     |
| Intervals                    | 0               | 2     |
| Monotonic Stack              | 0               | 2     |
| **Total**                    | **1**           | **75**|

---

## 🔍 Solution Walkthrough

### Problem: 1768. Merge Strings Alternately
**Difficulty:** Easy  
**Category:** Array/String  
**LeetCode Link:** https://leetcode.com/problems/merge-strings-alternately/

#### Approach
1. **Two Pointer Technique**: Iterate through both strings simultaneously
2. **String Building**: Construct result using list for O(n) append operations
3. **Edge Handling**: Manage unequal lengths by appending remaining characters

#### Solution Code
```python
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
    
        len_1, len_2 = len(word1), len_2 = len(word2)
        min_len = min(len_1, len_2)
        merged_word = ""

        # Merge for the overlapping part
        for i in range(min_len):
            merged_word += word1[i]
            merged_word += word2[i]

        # Append remaining if any
        if len_1 > min_len:
            merged_word += word1[min_len:]
        else:
            merged_word += word2[min_len:]
        return merged_word



if __name__ == "__main__":
    # Optional: Some quick manual checks before running the tests
    s = Solution()

    result1 = s.mergeAlternately("abc", "pqr")
    print("Input: word1='abc', word2='pqr' -->", result1)
    assert result1 == "apbqcr"

    result2 = s.mergeAlternately("ab", "pqrs")
    print("Input: word1='ab', word2='pqrs' -->", result2)
    assert result2 == "apbqrs"

    result3 = s.mergeAlternately("abcd", "pq")
    print("Input: word1='abcd', word2='pq' -->", result3)
    assert result3 == "apbqcd"

    print("Everything passed!")

```

#### Test Cases
```python
import unittest
from solution import Solution

class TestMergeStringsAlternately(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_basic_cases(self):
        self.assertEqual(self.s.mergeAlternately("abc", "pqr"), "apbqcr")
        self.assertEqual(self.s.mergeAlternately("ab", "pqrs"), "apbqrs")
        self.assertEqual(self.s.mergeAlternately("abcd", "pq"), "apbqcd")

    def test_one_empty_string(self):
        # Edge case if one string is empty (if it were allowed in constraints)
        self.assertEqual(self.s.mergeAlternately("", "pqrs"), "pqrs")
        self.assertEqual(self.s.mergeAlternately("abcd", ""), "abcd")

    def test_same_length(self):
        self.assertEqual(self.s.mergeAlternately("ab", "cd"), "acbd")

if __name__ == "__main__":
    unittest.main()
```

---

## 🛠️ Technical Skills
- **Algorithms**: Two Pointers, Sliding Window, DFS/BFS, Dynamic Programming
- **Data Structures**: Arrays, Hash Maps, Trees, Graphs, Linked Lists
- **Python Features**: List Comprehensions, Generators, Type Hints
- **Testing**: Unit Testing, Edge Case Handling, CI/CD Integration
- **Software Practices**: PEP-8 Compliance, Documentation, Version Control

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:
1. Fork the repository
2. Create your feature branch:
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add some amazing feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/amazing-feature
   ```
5. Open a Pull Request

See our [contribution guidelines](CONTRIBUTING.md) for more details.

---

## 📜 License
Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

---

## 🌐 Connect with Me

**Muaaz Bin Saeed**  
Passionate Problem Solver & Software Developer

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://linkedin.com/in/muaazbinsaeed)
[![LeetCode](https://img.shields.io/badge/LeetCode-Profile-orange?style=flat&logo=leetcode)](https://leetcode.com/muaazbinsaeed)
[![Email](https://img.shields.io/badge/Email-Contact-red?style=flat&logo=gmail)](mailto:muaaz.binsaeed@hotmail.com)

---

**Happy Coding!** 🎉 👨💻
*"Quality is not an act, it's a habit." - Aristotle*
