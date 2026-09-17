def fac(num):
    result=1
    for i in range(2,num+1):
        result*=i
    return result

#m=int(input('m='))
#n=int(input('n='))
m=5 
n=3


ans=fac(m)//fac(n)//fac(m-n)
print(f'ans={ans}')


from random import randrange
def roll_dice(DiceNumber=2):
    total=0
    for _ in range(1,DiceNumber+1):
        total+=randrange(1,7)
    return total

for _ in range(6):
    print(roll_dice())

# 用星号表达式来表示args可以接收0个或任意多个参数
# 调用函数时传入的n个参数会组装成一个n元组赋给args
# 如果一个参数都没有传入，那么args会是一个空元组
def add(*args):
    total=0
    for i in args:
        if type(i) in (int,float):
            total+=i
    return total
# 在调用add函数时可以传入0个或任意多个参数
print(add())         # 0
print(add(1))        # 1
print(add(1, 2, 3))  # 6
print(add(1, 2, 'hello', 3.45, 6))  # 12.4

def foo(*args,**kwargs):
    print(args)
    print(kwargs)
foo(3,2.1,'kk',name='骆昊', age=43, gpa=4.95)


import module1 as m1
import module2 as m2
m1.foo()
m2.foo()