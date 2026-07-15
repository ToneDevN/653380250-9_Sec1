# Week 1: Introduction to python & basic syntax

## What is python ? why python for scripting?

- Python is high level, interpreted, general purpose programming language
- Readability and simplicity ( pseudo-code like syntax ).
- Applications in scripting ( automation, web development, data analysis, AI/ML, etc ).

## Basic syntax :print(), comments, variables, data types

### Print() Functions

- Outputting information to the terminal.
**Example:**

```python
print("Hello, World!")  # Output: Hello, World!

name = "Nawamin"
print(f"Hello, {name}!")  # Output: Hello, Nawamin!
```

### Comments

- ใช้ `#` สำหรับ comment code ภายในบรรทัด
- ใช้ ` ''' ''' หรือ """ """ ` สำหรับ comment หลายบรรทัด

### Variables

python สามารถประกาศตัวแปรได้โดยไม่ต้องกำหนดชนิดของตัวแปร ( Dynamic typing )

### Data Types

| Data type | Description | Example |
| Integer (int) | จำนวนเต็ม | 1, -2, 0, 100 |
| Float (float) | จำนวนทศนิยม | 1.0, -2.5, 0.0, 100.5 |
| String (str) | ข้อความ | "Hello, World!", 'Python' |
| Boolean (bool) | จริงหรือเท็จ | True, False |

### Input/Output

- **Input() Function:** ใช้รับข้อมูลจากผู้ใช้
  - return เป็น string เสมอ (ต้องแปลงด้วย int() หรือ float())
