# 路径中不能有中文
'''
read()方法适用于文件较小的情况，当文件过大时会导致内存不足；
当读取大文件时，可以使用read(size)来规定每次读取的大小；
或者使用readline()每一行读取；
当读取配置文件时，可以使用readline()一次读取所有内容并按行返回list
'''
path = '/Users/apple/Documents/MyPython/PythonPractice/DailyPractice/IO.txt'
with open(path, 'r') as f:
    print(f.read())

# 'w'将会将前面的内容替换成下面的内容,'a'是在后面添加（append）内容
with open(path,'a') as f:
    f.write('\rHello,Lord')
