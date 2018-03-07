# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YycrawlItem(scrapy.Item):
    name = scrapy.Field()  # 名字
    honour = scrapy.Field()  # 等级1
    honourstar = scrapy.Field()  # 等级2
    noble = scrapy.Field()  # 等级3
    room = scrapy.Field()  # 直播间ID
    fm_id = scrapy.Field()  # 签约频道
    grade = scrapy.Field()  # 年度积分
    place = scrapy.Field()  # 位置
    impression = scrapy.Field()  # 印象
    fans = scrapy.Field()  # 粉丝数量
    follow = scrapy.Field()  # 关注数量
    url = scrapy.Field()  # 来源链接 之后根据来源链接 提取id 再去爬取视频、相册等数据
    u_id = scrapy.Field()


# 粉丝数据
class FansItem(scrapy.Item):
    author = scrapy.Field()  # 来源用户
    name = scrapy.Field()  # 粉丝名字
    image = scrapy.Field()  # 粉丝图片
    url = scrapy.Field()  # 粉丝主页链接


# 关注的人
class FollowItem(scrapy.Item):
    author = scrapy.Field()  # 来源用户
    name = scrapy.Field()  # 关注的人名字
    image = scrapy.Field()  # 关注的人图片
    url = scrapy.Field()  # 关注的人主页链接


"""
name  #名字
honour  #等级1
honourstar  #等级2
noble  #等级3
room  #直播间ID
fm_id  #签约频道
grade  #年度积分
place  #位置
impression  #印象
fans  #粉丝数量
follow  #关注数量
url  #来源链接 之后根据来源链接 提取id 再去爬取视频、相册等数据

author  #来源用户
name  #粉丝名字
image  #粉丝图片
url  #粉丝主页链接

author  #来源用户
name  #关注的人名字
image  #关注的人图片
url  #关注的人主页链接

"""
