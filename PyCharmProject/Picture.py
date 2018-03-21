import matplotlib.pyplot as plt
import math
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# 有中文出现的情况，需要u'内容'

# X轴取值范围
a = list(np.arange(0, 10, 0.1))
s1 = list(map(math.sin, a))
s2 = list(map(lambda v: math.sin(v - math.pi), a))
x = np.linspace(-30, 30, 1000)

# 正弦曲线
plt.plot(a, s1, label="SIN(X)")
# label等号后面显示的是在图表中的公式
plt.plot(a, s2, label="SIN(V-PI)")
# 抛物线
y = x**2 - 5*x + 10
plt.figure(figsize=(8, 4))
plt.plot(x, y, color="red", linewidth=2)
# X和Y轴的名字
plt.xlabel("Time(s)")
plt.ylabel("Volt")
# 图表名称
plt.title(u'抛物线示例图')
# Y轴的取值范围
plt.ylim(-100, 400)

plt.legend()
plt.show()
