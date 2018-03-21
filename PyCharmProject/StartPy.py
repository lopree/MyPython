# 测试自定义函数
from FuncPy import My_Abs, quadratic

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
