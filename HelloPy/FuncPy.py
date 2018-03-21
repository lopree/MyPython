import math
# 自定义绝对值函数


def My_Abs(x):
    if x > 0:
        return x
    else:
        return -x

# 求一元二次函数的根


def quadratic(a, b, c):
    if a != 0:
        dert = b**2 - 4*a*c
        if dert > 0:
            x1 = (-b + math.sqrt((b * b) - (4 * a * c))) / (2 * a)
            x2 = (-b - math.sqrt((b * b) - (4 * a * c))) / (2 * a)
            return x1, x2
        elif dert == 0:
            return -b/(2*a)
        else:
            return ('无实数根')
    else:
        return -c/b

# 可变参数


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

# 关键参数与命名关键字参数


def person01(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


def person02(name, age, *, city, job):
    print(name, age, city, job)

# 斐波拉契数列(01)


def fib01(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a+b
        n = n + 1
    return 'done'

# 斐波拉契数列(02)


def fib02(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b  # 换成yield就是另外一种定义生成器的形式
        a, b = b, a+b
        n = n + 1
    return 'done'

# 杨辉三角


def triangles():
    l = [1]
    while 1:
        yield l
        l = [1] + [l[n] + l[n+1] for n in range(len(l)-1)] + [1]
