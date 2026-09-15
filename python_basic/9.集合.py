# 集合的定义与运算
set1={1,2,3,3,3,2}
print(set1)

set2={'banana','pitaya','apple','banana','grape'}
print(set2)

set3=set('hellp')
print(set3)

set4=set({1, 2, 2, 3, 3, 3, 2, 1})
print(set4)

set5={num for num in range(1,20) if num %3==0 or num%7==0 }
print(set5)



set1={11,12,13,16}
print(11 in set1)
print(8 in set1)

if 16 in set1:
    print(16)


set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {2, 4, 6, 8, 10}

# 交集
print(set1&set2)
print(set1.intersection(set2))

# 并集
print(set1|set2)
print(set1.union(set2))

# 差集
print(set1-set2)
print(set1.difference(set2))

# 对称差
print(set1^set2)
print(set1.symmetric_difference(set2))


set1={1,10,100}
set1.add(1000)
set1.add(10000)
print(set1)

# 删除元素
set1.discard(10)
if 100 in set1:
    set1.remove(100)
print(set1)

set1.clear()
print(set1)


fset1=frozenset({1,3,5,7})
fset2=frozenset(range(1,6))

print(fset1)
print(fset2)
print(fset1&fset2)
print(fset1|fset2)
print(fset1-fset2)
print(fset1<fset2)
