"""
for-in  

"""

import time
for i in range(2):
    print("hello world")
    time.sleep(1)

#对于不用的变量,可以用下划线_代替
for _ in range(1):
    print("hello world")
    time.sleep(1)

"""
for 循环
"""
for i in range(1,100,2):
    print(i)
total=0
for i in range(1,101):
    total+=i
print(f'{total=}')
total=0
for i in range(2,101,2):
    total+=i
print(f'{total=}')
print(sum(range(1,101)))


"""
while 循环
"""

total=0
i=1
while i<=100:
    total+=i
    i+=1
print(f'{total=}')

"""
break and continue
"""

total=0;
i=2
while 1:
    if i>100:
        break
    total+=i
    i+=2
print(total)

total=0
for i in range(1,101):
    if i&1:
        continue
    total+=i;
print(total)

"""
嵌套循环结构
"""
for i in range(1,10):
    for j in range(1,i+1):
        print(f'{i}*{j}={i*j}',end='\t')
    print()

