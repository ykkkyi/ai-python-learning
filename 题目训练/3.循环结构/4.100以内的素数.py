for i in range(1,101):
    is_prime=1
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            is_prime=0
            break
    if is_prime:
        print(i)