# 学生成绩综合练习

[对应练习代码](<student_summary.py>)

### 思路与知识点

使用三个函数分别计算平均分、最高分学生和不及格学生列表，再集中输出。

### 运行说明与易错点

均值和最高分函数假定输入列表非空；筛选不及格学生的函数在没有匹配结果时返回空列表。

### 练习代码

```python
# Day 7: week 01 summary practice

students = [
    {"name": "Alice", "score": 92},
    {"name": "Bob", "score": 85},
    {"name": "Cindy", "score": 96},
    {"name": "David", "score": 58},
    {"name": "Eva", "score": 73},
]


def average_score(records):
    total = 0
    for student in records:
        total += student["score"]
    return total / len(records)


def find_top_student(records):
    top = records[0]
    for student in records:
        if student["score"] > top["score"]:
            top = student
    return top


def find_failed_students(records):
    failed = []
    for student in records:
        if student["score"] < 60:
            failed.append(student)
    return failed


avg = average_score(students)
top_student = find_top_student(students)
failed_students = find_failed_students(students)

print(f"平均分：{avg:.2f}")
print(f"最高分：{top_student['name']} ({top_student['score']})")

print("不及格学生：")
for student in failed_students:
    print(f"{student['name']}: {student['score']}")
```

### 检查结果

平均分为 `80.80`，最高分为 `Cindy (96)`，不及格学生为 `David: 58`。
