num=int(input("please enter a integer bumber:"))
is_prime=True
end=int(num**0.5)
print(f'end={end}')
for i in range(2,end+1):
    if num%i==0:
        is_prime=False
        break
if is_prime:
    print(f'{num}是素数')
else:
    print(f'{num}不是素数')