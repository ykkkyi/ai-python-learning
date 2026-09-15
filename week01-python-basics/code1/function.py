# Day 6: functions


def average(scores):
    return sum(scores) / len(scores)


def factorial(n):
    result = 1
    for number in range(1, n + 1):
        result *= number
    return result


def is_prime(n):
    if n <= 1:
        return False
    for number in range(2, int(n ** 0.5) + 1):
        if n % number == 0:
            return False
    return True


def count_words(text):
    words = text.lower().split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


scores = [88, 92, 75, 96, 84]
print("平均分：", average(scores))
print("5! =", factorial(5))
print("17 是素数吗？", is_prime(17))
print(count_words("python is useful python is easy"))

