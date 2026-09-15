a=float(input())
b=float(input())
c=float(input())
if a+b>c and a+c>b and b+c>a:
    p=(a+b+c)/2
    perimeter=a+b+c
    area=(p*(p-a)*(p-b)*(p-c))**0.5
    print(f'周长={perimeter}')
    print(f'面积={area}')
else:
    print("不能构成三角形")