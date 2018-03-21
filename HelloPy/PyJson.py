import json

data1 = {'rook':25,'stein':'Rook Stein','lopree':'www.baidu.com'}
# 将Python转化为json字符串
json_str = json.dumps(data1)

print('Python原内容：',repr(data1))
print('Json内容：',json_str)
# 将json字符串转化为Python
data2 = json.loads(json_str)
print("data2['stein']:",data2['stein'])