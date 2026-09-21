"""
算术运算符
"""
print(321 + 12)     # 加法运算，输出333
print(321 - 12)     # 减法运算，输出309
print(321 * 12)     # 乘法运算，输出3852
print(321 / 12)     # 除法运算，输出26.75
print(321 // 12)    # 整除运算，输出26
print(321 % 12)     # 求模运算，输出9
print(321 ** 12)    # 求幂运算，输出1196906950228928915420617322241



"""
海象运算符
Python 3.8 中引入了一个新的赋值运算符:=，我们称之为海象运算符，
。海象运算符也是将运算符右侧的值赋值给左边的变量，与赋值运算符不同的是
"""
# SyntaxError: invalid syntax
# print((a = 10))
# 海象运算符
print((a := 10))  # 10
print(a)          # 10


"""
比较运算符和逻辑运算符的使用
"""
flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag0
print('flag0 =', flag0)     # flag0 = True
print('flag1 =', flag1)     # flag1 = True
print('flag2 =', flag2)     # flag2 = False
print('flag3 =', flag3)     # flag3 = False
print('flag4 =', flag4)     # flag4 = True
print('flag5 =', flag5)     # flag5 = False
print(flag1 and not flag2)  # True
print(1 > 2 or 2 == 3)      # False