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
        dert = b ** 2 - 4 * a * c
        if dert > 0:
            x1 = (-b + math.sqrt((b * b) - (4 * a * c))) / (2 * a)
            x2 = (-b - math.sqrt((b * b) - (4 * a * c))) / (2 * a)
            return x1, x2
        elif dert == 0:
            return -b / (2 * a)
        else:
            return ('无实数根')
    else:
        return -c / b
