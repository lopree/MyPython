# 高阶函数
def doubleF(x):
    return x**2

r = map(doubleF,[1,2,3,4,5,6,7,8,9])
print(list(r))   

# 匿名函数
print(list(map(lambda x:x**2,[1,2,3,4,5,6,7,8,9])))