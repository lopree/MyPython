from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
import csv
import re

url = "http://hz.58.com/pinpaigongyu/pn/{page}/?minprice=1500_2000"
# 已完成的页码数 初始为0
page = 0

csv_file = open("rent.csv", "w", -1, "UTF-8")
csv_writer = csv.writer(csv_file, delimiter=',')
while True:
    page += 1
    print("fetch:", url.format(page=page))
    response = requests.get(url.format(page=page))
    # print("response:",response.text)
    html = BeautifulSoup(response.text, "html.parser")
    # print(html)
    house_list = html.select('.list > li')
    # print(house_list)

    # 循环到读不到新的房源页面为止
    if not house_list:
        break

    for house in house_list:
        house_title = house.select("h2")[0].string
        house_url = urljoin(url, house.select("a")[0]["href"])
        # 默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等
        house_info_list = house_title.split()
        # house_title.split()切割后的索引号为1的是地址
        house_location = house_info_list[1]
        # 判断房屋的类型————整租还是合租，在house_title.split()的索引号为0的string当中
        house_type = re.split('【|】', house_info_list[0])[1]
        # 房屋价格
        house_money = house.select(".money")[0].select("b")[0].string
        # 将分割读取好的数据写成一行数据
        csv_writer.writerow(
            [house_title, house_location, house_type,  house_money, house_url])


csv_file.close()
