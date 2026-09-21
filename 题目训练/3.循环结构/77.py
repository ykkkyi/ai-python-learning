
import random
money=int(input("请输入你带的金额："))
base=money
while money>0:
    print(f'你还有{money}元')
    print("继续游戏 1 ; 离开选择 0")
    choose=int(input("请输入你的选择："))
    if choose==0:
        break;
    while True:
        debt=int(input("输入你准备投入的金额："))
        if(0<=debt<=money):
            break
        elif money<debt:
            print("你没那么多钱了")
        else:
            print("输入金额错误")
    first_point=random.randrange(1,7)+random.randrange(1,7)
    print("你摇出了%d点"%first_point)
    if(first_point==7 or first_point==11):
        print("你赢了")
        money+=debt
    elif first_point==2 or first_point==3 or first_point==11:
        print("你输了")
        money-=debt
    else:
        while True:
            current_point=random.randrange(1,7)+random.randrange(1,7)
            print("你摇出了%d点"%current_point)
            if current_point==7:
                print("你输了")
                money-=debt
                break
            elif current_point==first_point:
                print("你赢了")
                money+=debt
                break
if money==0:
    print("你破产了")
else:
    if money>=base: print(f'恭喜你赢了{money-base}元')
    else : print(f'很遗憾你输了{base-money}元')


            
