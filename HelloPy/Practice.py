import re
stringNmae = "【整租】泊寓 文一路 万科泊寓文一"
print(stringNmae.split()[0])
print(type(stringNmae.split()[0]))
strFir = re.split('【|】',stringNmae.split()[0])[1]
print(strFir)
# print(type(strFir[0]))