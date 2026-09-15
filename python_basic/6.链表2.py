"""
一：添加和删除元素
"""

languages = ['python','java','c++']
print(languages)
languages.append('javascript')
print(languages)
languages.insert(1,'SQL')
print(languages)

languages = ['Python', 'SQL', 'Java', 'C++', 'JavaScript']
if 'Java' in languages:
    languages.remove('Java')
if 'Swift' in languages:
    languages.remove('Swift')
print(languages)  # ['Python', 'SQL', C++', 'JavaScript']
languages.pop()
temp = languages.pop(1)
print(temp)       # SQL
languages.append(temp)
print(languages)  # ['Python', C++', 'SQL']
languages.clear()
print(languages)  # []

"""
remove
"""

example=['pp','aa','pp']
example.remove('pp')   #若链表中有多个'pp',list.remove('pp')会删除第一个
print(example)

#del和pop的区别
"""
就是使用 Python 中的del关键字后面跟要删除的元素，这种做法跟使用pop方法指定索引删除元素没有实质性的区别，
但后者会返回删除的元素，前者在性能上略优，因为del对应的底层字节码指令是DELETE_SUBSCR，而pop对应的底层字节码指令是CALL_METHOD和POP_TOP
"""

iteas=['Python','Java','C++']
del iteas[1]
print(iteas)


"""
二：元素位置和频次

"""

items = ['Python', 'Java', 'Java', 'C++', 'Kotlin', 'Python']
print(items.index('Python'))
print(items.index('Python',1))
print(items.count('Python'))
print(items.count('C++'))
print(items.count('yky'))

# 从索引位置3开始查找'Java'
#print(items.index('Java', 3))    # ValueError: 'Java' is not in list

"""
三：元素排序和反转
"""

items=[23,87,32.6,99,6,3,31]
print(items)
items.sort()
print(items)
items.reverse()
print(items)

"""
四：列表生成式
"""

#1
items=[]
for i in range(1,100):
    if i%3==0 or i%5==0:
        items.append(i)
print(items)

items1=[i for i in range(1,100) if i%3==0 or i%5==0]
print(items1)

#2
num1=[35, 12, 97, 64, 55]
num2=[]
for x in num1:
    num2.append(x**2)
print(num2)

num3=[x**2 for x in num1 ]
print(num3)


#3
nums1 = [35, 12, 97, 64, 55]
nums2 = []
for num in nums1:
    if num > 50:
        nums2.append(num)
print(nums2)

num3=[x for x in num1 if x>50]
print(num3)

"""
嵌套列表
"""

scores = [[95, 83, 92], [80, 75, 82], [92, 97, 90], [80, 78, 69], [65, 66, 89]]
print(scores[0])
print(scores[0][1])


import random

scores=[]
for _ in range(5):
    tmp=[]
    for _ in range(3):
        score=random.randint(1,100)
        tmp.append(score)
    scores.append(tmp)

print(scores)


scores=[[random.randrange(60,101) for _  in range(3)] for _ in range(5)]
print(scores)