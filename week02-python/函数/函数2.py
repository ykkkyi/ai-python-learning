def calc(init_value,op_func,*args,**kwargs):
    items=list(args)+list(kwargs.values())
    result=init_value
    for x in items:
        if type(x) in (int , float):
            result=op_func(result,x)
    return result

def add(x,y):
    return x+y
def mul(x,y):
    return x*y

print(calc(0,add,1,2,3,4,5,6))
print(calc(1,mul,1,2,3,4,5,6))


old_nums = [35, 12, 8, 99, 60, 52]
new_nums=list(map(lambda x:x**2,filter(lambda x:x%2==0,old_nums)))
print(new_nums)


import functools
import operator
# 用一行代码实现计算阶乘的函数
fac = lambda n:functools.reduce(operator.mul,range(2,n+1),1)
# 用一行代码实现判断素数的函数
is_prime = lambda x:all(map(lambda f:x%f,range(2,int(x**0.5)+1)))
print(fac(6))
print(is_prime(37))

int2 = functools.partial(int,base=2)
int8 = functools.partial(int,base=8)
int16 = functools.partial(int,base=16)

s='1010'
print(int(s))
print(int2(s))
print(int8(s))
print(int16(s))
