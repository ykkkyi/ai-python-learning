# 列表索引与增删

[对应练习代码](<list.py>)

### 思路与知识点

练习长度、正负索引、追加、插入、弹出元素，以及保存混合类型和嵌套列表。

### 运行说明与易错点

嵌套列表在外层只占一个元素位置。索引超出范围会抛出 `IndexError`。

### 练习代码

```python
classmates=["小明","小红","小白"]
print(classmates)
#变量classmates就是一个list。用len()函数可以获得list元素的个数
print(len(classmates))
print(classmates[0],classmates[1],classmates[2],',')

print(classmates[-1])
#当索引超出了范围时，Python会报一个IndexError错误，所以，要确保索引不要越界，记得最后一个元素的索引是len(classmates) - 1。
#如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：

print(classmates[-2])
print(classmates[-3])

classmates.append('Adam')
#list是一个可变的有序表，所以，可以往list中追加元素到末尾：
classmates.insert(1,'yky')

classmates.pop()
#要删除list末尾的元素，用pop()方法
classmates.pop(1)
#要删除指定位置的元素，用pop(i)方法，其中i是索引位置

L = ['Apple', 123, True , 2.2213]
#list里面的元素的数据类型也可以不同
s=['python','java',['asp','php'],'cpp']
print(len(s))
s.append(True)
print(len(s))
s.insert(2,3.1212)
print(len(s))
print(s)


L=[]
print(len(L))
```

### 检查结果

初始同学列表长度为 3；嵌套列表 `s` 的长度依次为 4、5、6；空列表长度为 0。
