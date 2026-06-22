print(ord('A'))
print(ord('中'))
print(chr(66))
#Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：


print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))

print(b'ABC'.decode('ascii'))


print(len('ABC'))
print(len('中文'))
#str包含多少个字符，可以用len()函数

print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))
#len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：



print('age: %d' % (15))
print('%.2f' % 3.11221)
print("grow rate: %f %%"%(4.3232))
#%运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略
#如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串

print('hello,{0},成绩提升了{1:.2f}'.format('yky',77.989))
#另一种格式化字符串的方法是使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……，不过这种方式写起来比%要麻烦得多：

r=2.5
s=3.14*r**2
print(f'the area of a circle with radius {r} is {s}')
#最后一种格式化字符串的方法是使用以f开头的字符串，称之为f-string，它和普通字符串不同之处在于，字符串如果包含{xxx}，就会以对应的变量替换：

s1=72
s2=85
r=(s2-s1)/s1
print('提升%.1f %%'%(r))
print('提升{0:.1f} %'.format((s2-s1)/s1))
print(f'提升{r:.1f} %')