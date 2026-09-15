

x=int(input('x='))
y=int(input('y='))
for i in range(x,0,-1):
    if x%i==0 and y%i==0:
        print(f'最大公约数是{i}')
        break

x=int(input('x='))
y=int(input('y='))
while y!=0:
    tmp=x%y
    x=y
    y=tmp
print(f'最大公约数是{x}')
