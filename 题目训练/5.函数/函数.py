import random
import string
ALL_chars=string.ascii_letters+string.digits
def generate_code(*,code_len=4):   #*：后面的参数必须写参数名传入
    return ''.join(random.choices(ALL_chars,k=code_len))

for _ in range(5):
    print(generate_code())
for _ in range(6):
    print(generate_code(code_len=7))


def is_prime(num)->bool:
    for i in range(2,int(num**(0.5)+1)):
        if(num%i==0):
            return False
    return True


def gcd(x:int,y:int)->int:
    while y%x!=0:
       x,y=y,x%y
    return x
def lcm(x:int,y:int)->int:
    return x*y//gcd(x,y)


"""极差（全距）"""
def ptp(data):   #传入一个链表
    return max(data)-min(data)

"""算术平均"""
def mean(data):
    return sum(data)/len(data)

"""中位数"""
def median(data):
    tmp=sorted(data)
    size=len(data)
    if(size&1):
        return tmp[size//2]
    else:
        return mean(tmp[size//2-1:size//2+1])    #链表的切片
    
"""方差"""
def var(data):
    x_bar=mean(data)
    tmp=[(num-x_bar)**2 for num in data]
    return sum(tmp)/(len(tmp)-1)

"""标准差"""
def std(data):
    return var(data)**0.5;

"""变异系数"""
def cv(data):
    return std(data) / mean(data)

def describe(data):
    """输出描述性统计信息"""
    print(f'均值: {mean(data)}')
    print(f'中位数: {median(data)}')
    print(f'极差: {ptp(data)}')
    print(f'方差: {var(data)}')
    print(f'标准差: {std(data)}')
    print(f'变异系数: {cv(data)}')

f=[0,5,6,7,4,5,6,8,6]
describe([1,4,6,7,8,8,9])
describe(f)

import random
red_balls=[i for i in range(1,34)]
blue_balls=[i for i in range(1,17)]

def choice():
    selected_balls=random.sample(red_balls,6)
    selected_balls.sort()
    selected_balls.append(random.choice(blue_balls))
    return selected_balls

def display(selected_balls):
    for ball in selected_balls:
         print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
    print(f'\033[034m{selected_balls[-1]:0>2d}\033[0m')

for _ in range(5):
    display(choice())
