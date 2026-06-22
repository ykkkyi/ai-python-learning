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

