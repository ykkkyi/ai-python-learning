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

