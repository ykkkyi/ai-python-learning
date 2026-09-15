
"""
元组和列表的不同之处在于，元组是不可变类型，
这就意味着元组类型的变量一旦定义，其中的元素不能再添加或删除，而且元素的值也不能修改。
如果试图修改元组中的元素，将引发TypeError错误，导致程序崩溃。
定义元组通常使用形如(x, y, z)的字面量语法，
元组类型支持的运算符跟列表是一样的
"""



t1 = (35,12,98)
t2 = ('yky',45,True,'kk')

# 查看变量的类型
print(type(t1))
print(type(t2))

# 查看元组中元素的数量
print(len(t1))
print(len(t2))

# 索引运算
print(t1[0])
print(t2[2])
print(t2[-1])


# 切片运算
print(t1[:2])
print(t2[::3])

# 循环遍历元组中的元素
for index in range(len(t1)):
    print(t1[index])
for elem in t2:
    print(elem)

# 成员运算
print(12 in t1)         # True
print(99 in t1)         # False
print('Hao' not in t2)  # True

# 拼接运算
t3 = t1 + t2
print(t3)  # (35, 12, 98, '骆昊', 45, True, '四川成都')

# 比较运算
print(t1 == t3)            # False
print(t1 >= t3)            # False
print(t1 <= (35, 11, 99))  # False



"""
()表示空元组，但是如果元组中只有一个元素，需要加上一个逗号，否则()就不是代表元组的字面量语法，而是改变运算优先级的圆括号，
所以('hello', )和(100, )才是一元组，而('hello')和(100)只是字符串和整数
"""
a = ()
print(type(a))  # <class 'tuple'>
b = ('hello')
print(type(b))  # <class 'str'>
c = (100)
print(type(c))  # <class 'int'>
d = ('hello', )
print(type(d))  # <class 'tuple'>
e = (100, )
print(type(e))  # <class 'tuple'>


"""
打包和解包操作
"""

#打包操作
a=1,10,'yky'
print(type(a))
print(a)

#解包操作
x,y,z=a
print(x,y,z)

#解包时个数不对应
a = 1, 10, 100, 1000
# i, j, k = a             # ValueError: too many values to unpack (expected 3)
# i, j, k, l, m, n = a    # ValueError: not enough values to unpack (expected 6, got 4)



#解包时 通过星号表达式可以把多个元素赋给一个变量，用星号表达式修饰的变量会变成一个列表
a=1,10,100,'yky'
i,j,*k=a
print(i,j,k)
i,*j,k=a
print(i,j,k)
i,*j=a
print(i,j,k)
i,j,k,*m=a
print(i,j,k,m)
i,j,k,m,*n=a
print(i,j,k,m,n)
n.append('kk')
print(n)


#解包语法对所有的序列都成立，这就意味着我们之前讲的列表、range函数构造的范围序列甚至字符串都可以使用解包语法

a, b, *c =[i for i in range(1,10) if i&1] 
print(a, b, c)
a, b, c = [1, 10, 100]
print(a, b, c)
a, *b, c = 'hello'
print(a, b, c)


"""
交换变量的值
"""
a=11
b=12
c=13
a, b = b, a
a, b, c = b, c, a


"""
元组和列表的比较

1.元组是不可变类型，不可变类型更适合多线程环境，因为它降低了并发访问变量的同步化开销

2.元组是不可变类型，通常不可变类型在创建时间上优于对应的可变类型

"""
import timeit
print('%.3f 秒' % timeit.timeit('[1,2,3,4,5,6,7,8,9]',number=1000000))
print('%.3f 秒' % timeit.timeit('(1,2,3,4,5,6,7,8,9)',number=1000000))


infos=('yky',11,True)
print(infos)
print(list(infos))