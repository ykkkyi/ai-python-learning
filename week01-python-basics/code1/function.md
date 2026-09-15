# 函数练习：均值、阶乘、素数与词频

[对应练习代码](<function.py>)

### 思路与知识点

将重复计算组织成函数，通过参数传入数据，用 `return` 返回结果。

### 运行说明与易错点

`average` 要求列表非空，`factorial` 的学习范围为非负整数；`is_prime` 已处理小于等于 1 的输入。此处词频函数按空格拆词，没有额外剥离标点。

### 练习代码

```python
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
```

### 检查结果

均值为 `87.0`，`5!` 为 `120`，17 是素数；词频中 python 和 is 各出现 2 次。
