
import random
money=1000
while money>0:
    print("你现在有%d元钱"%money)
    while 1:
        debt=int(input("请输入你要下注的金额："))
        if 0<=debt<=money:
            break
    first_point=random.randrange(1,7)+random.randint(1,7)
    print(f'摇出了{first_point}')
    if first_point ==7 or first_point==11:
        print(f'你赢了{debt}元钱 ')
        money+=debt
    elif first_point==2 or first_point==3 or first_point==12:
        print(f'你输了{debt}元钱')
        money-=debt
    else:
        while True:
            current_point=random.randrange(1,7)+random.randrange(1,7)
            print(f'你又摇出了{current_point}点')
            if current_point==first_point:
                print(f'你赢了{debt}元钱 ')
                money+=debt
                break
            elif current_point==7:
                print(f'你输了{debt}元钱')
                money-=debt
                break
print('你破产了, 游戏结束!')
            
        

