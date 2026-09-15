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

