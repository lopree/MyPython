# 测试自定义函数
from FuncPy import My_Abs, quadratic, calc, person01, person02, fib01, fib02,triangles
print(100 + 200)
# 字符串
print('I\'m \"OK\"!')
# list和tuple
MyName = ['Rook', 'Stein', 'lopree']
print(MyName)
print(len(MyName))
print(MyName[0])
MyName.append('rook stein')  # 在list最后添加一个元素
MyName.pop()  # 删除最后一个元素，pop(i):删除指定索引位置的元素
MyName[0] = 'Rook Stein'  # 替换元素
print(MyName)
print(MyName[-1])  # 打印list最后一个元素，-2为倒数第二个

# tuple和list非常类似，但是tuple一旦初始化就不能修改，如果可能，能用tuple代替list就尽量用tuple。
t = (1,)  # 只有一个元素时需注意加逗号
t1 = (1, 3, ['rook', 3])
t1[2][0] = 666  # 实质上改的时list里面的元素
t1[2][1] = 'stein'
print(t1)

# dict
d = {'rook': 91, 'stein': 80, 'lopree': 60}
print(d['rook'])
d['Rook Stein'] = 80  # 可直接添加
print(d)
# 判断key值是否存在的两种方法：
print('asd' in d)
# d.get('sad')返回None值，在Python中不显示，后面加上数值则判断不存在时返回该值
print(d.get('asd', -1))

# set
s = set([1, 2, 3])
print(s)
# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
s.add(4)
s.add(4)
print(s)
s1 = set([1, 2, 3])
s2 = set([2, 4, 6])
print(s1 & s2)
print(s1 | s2)


# 测试自定义函数
print(My_Abs(-5))
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
# 可变参数函数
print(calc(1, 2, 3))
num = [1, 2, 3]
print(calc(*num))
# 关键参数与命名关键字参数
person01('rook', 25, city='杭州')
person01('stein', 20, city='Chemnitz', job='Student')
extra = {'city': 'Chemnitz', 'gender': 'M', 'job': 'Student'}
person01('柳驰', 26, **extra)
person01('翟佳林', 26, **extra)

# 1.列表生成式
# 10以内的偶数的平方
print([x*x for x in range(1, 11) if x % 2 == 0])
# 两层循环创造全排列
print([m + n for m in 'ABC' for n in 'XYZ'])
# 两个变量生成list以及小写list中的元素
d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()])
L = ['Hello', 'APPLE', 'BMI', 'IBm']
print([s.lower() for s in L])
# 2.生成器
print(fib01(6))
# 但是无法获得fib02中return的值
for nn in fib02(6):
    print(nn)
# 改进
g = fib02(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

# 2.1杨辉三角
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10: 
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')