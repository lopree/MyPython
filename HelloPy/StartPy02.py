import time
localtime = time.asctime(time.localtime(time.time()))
print("当地时间：",localtime)
# 格式化成20XX-月份-日 时:分:秒形式
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
  
# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print (time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))

# 获取某月的日历
import calendar
cal = calendar.month(2018,3)
print ("以下输出2018年3月份的日历:")
print(cal)