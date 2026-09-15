person = {'name': '王大锤', 'age': 55, 'height': 168, 'weight': 60, 'addr': '成都市武侯区科华北路62号1栋101'}
# 成员运算
print('name' in person)
print('tal' in person)

# 索引
print(person['name'])
print(person['addr'])
person['age']=25
person['height']=178
person['signature']='你的男朋友是一个盖世垃圾，他会踏着五彩祥云去迎娶你的闺蜜'
print(person)

# 循环遍历
for key in person:
    print(f'{key}:\t{person[key]}')


person = {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都'}
print(person.keys())
print(person.values())
print(person.items())

for key,value in person.items():
    print(f'{key}:\t{value}')


person = {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
print(person.pop('age'))
print(person.popitem())
for key,value in person.items():
    print(f'{key}:{value}')



sentence = input('please enter a sentence:')
cnt={}
for ch in sentence:
    if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
        cnt[ch]=cnt.get(ch,0)+1

sorted_cnt=sorted(cnt,key=cnt.get,reverse=True)
for key in sorted_cnt:
    print(f'{key} 出现了 {cnt[key]} 次.')