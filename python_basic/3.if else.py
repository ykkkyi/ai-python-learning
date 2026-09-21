

#BMI计算器
height=float(input())
weight=float(input())
bmi=weight/((height/100)**2)
print(f'{bmi=:.1f}')
if 18.5<=bmi<24:
    print('你的身体很棒')

"""
BMI计算器
"""
height = float(input('身高(cm):'))
weight = float(input('体重(kg):'))
bmi = weight / (height / 100) ** 2
print(f'{bmi = :.1f}')
if 18.5 <= bmi < 24:
    print('你的身材很棒！')
else:
    print('你的身材不够标准哟！')



"""
BMI计算器
"""
height = float(input('身高(cm):'))
weight = float(input('体重(kg):'))
bmi = weight / (height / 100) ** 2
print(f'{bmi = :.1f}')
if bmi < 18.5:
    print('你的体重过轻！')
elif bmi < 24:
    print('你的身材很棒！')
elif bmi < 27:
    print('你的体重过重！')
elif bmi < 30:
    print('你已轻度肥胖！')
elif bmi < 35:
    print('你已中度肥胖！')
else:
    print('你已重度肥胖！')



status_code=int(input('please enter a status_code:'))
match status_code:
    case 400:description="Bad request"
    case 401:description="Unauthorized"
    case 403:descripyion="Forbindden"
    case 404:description="Not found"
    case 405:description="Method not allowed"
    case 418:description="I am a teapot"
    case 429:description="Too many requests"
print('状态码描述',description)



status_code = int(input('响应状态码: '))
match status_code:
    case 400 | 405: description = 'Invalid Request'
    case 401 | 403 | 404: description = 'Not Allowed'
    case 418: description = 'I am a teapot'
    case 429: description = 'Too many requests'
    case _: description = 'Unknown Status Code'
print('状态码描述:', description)
