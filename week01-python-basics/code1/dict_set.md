# 字典与集合练习

[对应练习代码](<dict_set.py>)

### 思路与知识点

遍历姓名到分数的映射，用循环寻找最高分，再用集合对重复姓名去重。

### 运行说明与易错点

字典适合保存关联关系，集合适合去重与成员判断。这里的最高分查找假定分数非负。

### 练习代码

```python
# Day 4: dict and set

students = {
    "Alice": 92,
    "Bob": 85,
    "Cindy": 96,
    "David": 78,
}

print("所有学生成绩：")
for name, score in students.items():
    print(f"{name}: {score}")

best_name = ""
best_score = -1
for name, score in students.items():
    if score > best_score:
        best_name = name
        best_score = score

print(f"最高分学生：{best_name}, 分数：{best_score}")

names = ["Alice", "Bob", "Alice", "Cindy", "Bob"]
unique_names = set(names)
print("去重后的姓名：", unique_names)
```

### 检查结果

最高分为 `Cindy, 96`；去重后包含 Alice、Bob、Cindy，显示顺序不固定。
