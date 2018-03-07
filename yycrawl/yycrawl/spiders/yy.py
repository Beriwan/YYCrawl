# -*- coding: utf-8 -*-
import scrapy, re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from yycrawl.items import  YycrawlItem
# FansItem, FollowItem,

class YySpider(CrawlSpider):
    name = 'yy'
    allowed_domains = ['yy.com']
    start_urls = ['http://www.yy.com/', "http://www.yy.com/u/follow/1596032043#follow"]

    rules = (
        Rule(LinkExtractor(allow=r'follow/'), follow=True),
        Rule(LinkExtractor(allow=r'videos/'), follow=True),
        Rule(LinkExtractor(allow=r'music/'), follow=True),
        Rule(LinkExtractor(allow=r'u/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response.url)
        item = YycrawlItem()
        item["name"] = "".join(response.xpath('/html/body/div[2]/div/div[2]/div[1]/h1/text()').extract())  # 名字
        item["honour"] = "".join(
            response.xpath('/html/body/div[2]/div/div[2]/div[1]/div[1]/i[1]/@class').extract())  # 等级1
        item["honourstar"] = "".join(
            response.xpath('/html/body/div[2]/div/div[2]/div[1]/div[1]/i[2]/@class').extract())  # 等级2
        item["noble"] = "".join(response.xpath('/html/body/div[2]/div/div[1]/div[2]/span/text()').extract())  # 等级3
        item["room"] = "".join(
            response.xpath('/html/body/div[2]/div/div[2]/div[2]/div[1]/span[1]/text()').extract())  # 直播间ID
        item["fm_id"] = "".join(
            response.xpath('/html/body/div[2]/div/div[2]/div[2]/div[1]/span[3]/text()').extract())  # 签约频道
        item["grade"] = "".join(
            response.xpath('/html/body/div[2]/div/div[2]/div[2]/div[1]/span[5]/text()').extract())  # 年度积分
        item["place"] = "".join(
            response.xpath('/html/body/div[2]/div/div[2]/div[2]/div[1]/span[7]/text()').extract())  # 位置
        item["impression"] = "|".join(
            response.xpath('/html/body/div[2]/div/div[2]/div[2]/div[2]/a/text()').extract())  # 印象
        item["fans"] = "".join(response.xpath('/html/body/div[2]/div/div[4]/a[1]/span/text()').extract())  # 粉丝数量
        item["follow"] = "".join(response.xpath('/html/body/div[2]/div/div[4]/a[2]/span/text()').extract())  # 关注数量
        item["url"] = "".join(response.url)  # 来源链接 之后根据来源链接 提取id 再去爬取视频、相册等数据

        item["u_id"] = "".join(re.findall(re.compile(r'u/([0-9]{1,20})'), response.url))
        print(item)
        return item


"""
    def parse_follow(self, response):
        follow_item = FollowItem()
        u_id = response.meta["u_id"]
        follow_item["author"] = response.meta["name"]  # 来源用户
        follow_item["name"] = "".join(response.xpath('').extract())  # 关注的人名字
        follow_item["image"] = "".join(response.xpath('').extract())  # 关注的人图片
        follow_item["url"] = "".join(response.xpath('').extract())  # 关注的人主页链接
        yield scrapy.Request(url="http://www.yy.com/u/follow/{}#follow".format(u_id),
                             meta={"name": follow_item["name"],"u_id":u_id},
                             callback=self.parse_fans, encoding='utf-8')
        return follow_item

    def parse_fans(self, response):
        fans_item = FansItem()
        fans_item["author"] = "".join(response.xpath('').extract())  # 来源用户
        fans_item["name"] = "".join(response.xpath('').extract())  # 粉丝名字
        fans_item["image"] = "".join(response.xpath('').extract())  # 粉丝图片
        fans_item["url"] = "".join(response.xpath('').extract())  # 粉丝主页链接
        print(fans_item)
        return fans_item
"""
