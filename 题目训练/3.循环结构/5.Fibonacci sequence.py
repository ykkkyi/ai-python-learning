pref1=1
pref2=1
print(pref1)
print(pref2)
for i in range(3,21):
    pref1,pref2=pref2,pref1+pref2
    print(pref2)
