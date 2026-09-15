# 基本语法综合示例

[对应练习代码](<basic_syntax.py>)

### 思路与知识点

一次练习变量、字符串方法、列表统计和字典访问。

### 运行说明与易错点

`sorted(numbers)` 返回新列表；`student['name']` 按键读取字典的值。

### 练习代码

```python
name = "AI learner"
age = 18
gpa = 4.0
is_student = True

print("Name:", name)
print("Age:", age)
print("GPA:", gpa)
print("Is student:", is_student)

message = "Python is useful for AI research."
print("Message length:", len(message))
print("First word:", message.split()[0])
print("Lowercase:", message.lower())

numbers = [3, 1, 4, 1, 5, 9]
print("Numbers:", numbers)
print("Sum:", sum(numbers))
print("Max:", max(numbers))
print("Sorted:", sorted(numbers))

student = {
    "name": "Alice",
    "major": "Artificial Intelligence",
    "score": 92,
}
print("Student:", student)
print("Student name:", student["name"])
```

### 检查结果

列表之和为 `23`，最大值为 `9`，排序结果为 `[1, 1, 3, 4, 5, 9]`；学生名为 Alice。
