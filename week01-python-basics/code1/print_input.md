# 输出、输入与字符串表示

[对应练习代码](<print_input.py>)

### 思路与知识点

综合练习 `print`、转义字符、原始字符串、多行字符串、输入和两种除法。

### 运行说明与易错点

`print` 默认在参数之间插入空格，在末尾换行。大写命名 `PI` 只是常量命名约定，Python 不会阻止再次赋值。

### 练习代码

```python
print('hello','world','yky')       
#print()会依次打印每个字符串，遇到逗号,会输出一个空格，因此，输出的字符串是这样拼起来的

print('100+200=',100+200)


print('I\'m\"OK\"!\n')
#字符串是以单引号'或双引号"括起来的任意文本
#转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\
print('I\'m learning\nPython\n')
print('\\\n\\\n')
print('\\\t\\\n')



print(r'\\n\\n\\t')
#Python还允许用r''表示''内部的字符串默认不转义

print('''line1
line2
line3''')
#Python允许用'''...'''的格式表示多行内容


print(r'''hello,\n
world''')
#\n不转义 ''' '''有效


#输出为
"""hello world yky
100+200= 300
I'm"OK"!

I'm learning
Python

\
\

\       \

\\n\\n\\t
line1
line2
line3


"""

name=input()
print("the name is",name)
#输出：
#yky
#the name is yky
"""
name=input()
print('hello',name)
"""

name=input('please enter your name: ')
print(name)

print('1024*768=',1024*768)


n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Bob!'''
print(n)
print(f)
print(s1)
print(s2)
print(s3)
print(s4)


print(10/3,9/3,9//3,10//3)
#/除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数
#还有一种除法是//，称为地板除，两个整数的除法仍然是整数
PI = 3.14159265359
PI=1
print(PI)
```

### 检查结果

需要输入两次姓名；`1024*768` 为 `786432`；`10/3` 为浮点数，而 `10//3` 为整数 3。
