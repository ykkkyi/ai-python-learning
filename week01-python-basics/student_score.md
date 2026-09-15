# 学生成绩统计

[对应练习代码](<student_score.py>)

### 思路与知识点

用列表保存多名学生，每名学生用字典表示；分别通过函数计算平均分和寻找最高分。

### 运行说明与易错点

当前两个函数假定列表非空，空列表分别会导致除零或索引越界。`if __name__ == '__main__'` 使主流程只在直接运行脚本时执行。

### 练习代码

```python
students = [
    {"name": "Alice", "score": 92},
    {"name": "Bob", "score": 85},
    {"name": "Cindy", "score": 96},
    {"name": "David", "score": 78},
]


def average_score(records):
    total = 0
    for student in records:
        total += student["score"]
    return total / len(records)


def top_student(records):
    best = records[0]
    for student in records:
        if student["score"] > best["score"]:
            best = student
    return best


def main():
    avg = average_score(students)
    best = top_student(students)

    print(f"Average score: {avg:.2f}")
    print(f"Top student: {best['name']} ({best['score']})")


if __name__ == "__main__":
    main()
```

### 检查结果

输出平均分 `87.75`，最高分学生 `Cindy (96)`。
