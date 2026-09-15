# 分支与对象的真值

[对应练习代码](<if_loop.py>)

### 思路与知识点

根据年龄选择分支，再用 `if x` 判断一个对象是否为真。

### 运行说明与易错点

后半段连续给 `x` 赋值，最终被判断的是 `(1,)`。当前文件虽叫 if_loop，但尚未包含循环示例；循环可参考基础笔记 [循环结构](<../../python_basic/4.循环结构.md>)。

### 练习代码

```python
age=int(input('please enter your age:'))
if age >= 18:
    print("adult")
elif age>=6:
    print("teenager")
else:
    print("kid")


x=1
x='s'
x=[1,2,3]
x=(1,)
if x:
    print('True')
```

### 检查结果

输入 `18` 输出 adult，输入 `6` 输出 teenager，输入 `5` 输出 kid；最后都输出 True。
