# coding:utf-8
import requests
import re
from lxml import etree

# url = "http://www.yy.com/u/follow/1596032043#follow"
url = "http://www.yy.com/u/follow/1596032043"
response = requests.get(url)
response.encoding = 'utf-8'
print(response.text)
item = {}

response = etree.HTML(response.text)
href = response.xpath('//a/@href')
print(href)
# item["name"] = "".join(response.xpath('/html/body/div[2]/div/div[2]/div[1]/h1/text()'))  # 名字
# item["honour"] = "".join(
#     response.xpath('/html/body/div[2]/div/div[2]/div[1]/div[1]/i[1]/@class'))  # 等级1
# item["honourstar"] = "".join(
#     response.xpath('/html/body/div[2]/div/div[2]/div[1]/div[1]/i[2]/@class'))  # 等级2
# item["noble"] = "".join(response.xpath('/html/body/div[2]/div/div[1]/div[2]/span/text()'))  # 等级3
# item["room"] = "".join(
#     response.xpath('/html/body/div[2]/div/div[2]/div[2]/div[1]/span[1]/text()'))  # 直播间ID
# item["fm_id"] = "".join(
#     response.xpath('/html/body/div[2]/div/div[2]/div[2]/div[1]/span[3]/text()'))  # 签约频道
# item["grade"] = "".join(
#     response.xpath('/html/body/div[2]/div/div[2]/div[2]/div[1]/span[5]/text()'))  # 年度积分
# item["place"] = "".join(
#     response.xpath('/html/body/div[2]/div/div[2]/div[2]/div[1]/span[7]/text()'))  # 位置
# item["impression"] = "|".join(
#     response.xpath('/html/body/div[2]/div/div[2]/div[2]/div[2]/a/text()'))  # 印象
# item["fans"] = "".join(response.xpath('/html/body/div[2]/div/div[4]/a[1]/span/text()'))  # 粉丝数量
# item["follow"] = "".join(response.xpath('/html/body/div[2]/div/div[4]/a[2]/span/text()'))  # 关注数量
# item["url"] = "".join(url)  # 来源链接 之后根据来源链接 提取id 再去爬取视频、相册等数据
#
item["u_id"] = "".join(re.findall(re.compile(r'u/([0-9]{1,20})'), url))
print(item)
