# 1.使用内建函数isinstance将list中的元素小写
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')

# 2.练习判断语句
height = input('输入您的身高：')
weight = input('输入您的体重：')
h = float(height)
w = float(weight)
BMI = w / h**2
if BMI < 18.5:
    print('过轻')
elif BMI < 25:
    print('正常')
elif BMI < 28:
    print('过重')
elif BMI < 32:
    print('肥胖')
else:
    print('严重肥胖')
