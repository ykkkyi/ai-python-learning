import random
answer=random.randrange(1,101)
counter=0
while 1:
    counter+=1
    num=int(input('请输入：'))
    if num>answer: 
        print('大了')
    elif num<answer:
        print('小了')
    else:
        print('猜对了')
        break
print(f'你总共猜了{counter}次')