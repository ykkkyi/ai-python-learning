# 输入、变量与类型转换

[对应练习代码](<day1_basic.py>)

### 思路与知识点

读取姓名和年龄，将年龄转换为整数，再用格式化字符串输出。

### 运行说明与易错点

输入年龄时如果填写无法转成整数的文本，`int` 会抛出 `ValueError`。

### 练习代码

```python
# Day 1: print, input, variables, and basic types

name = input("请输入你的名字：")
age = int(input("请输入你的年龄："))

print(f"你好，{name}")
print(f"你今年 {age} 岁")
print(f"明年你 {age + 1} 岁")
print("name 的类型是：", type(name))
print("age 的类型是：", type(age))
```

### 检查结果

输入 `Alice`、`18`，应显示明年 19 岁，姓名类型为 `str`，年龄类型为 `int`。
