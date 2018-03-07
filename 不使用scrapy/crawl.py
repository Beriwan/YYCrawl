# coding:utf-8
import requests
import re, json
from lxml import etree


# 获取网页代码
def get_response(url):
    DEFAULT_REQUEST_HEADERS = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en',
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Host": "www.yy.com",
        # "Referer": url,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
                        Chrome/64.0.3282.168 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }
    response = requests.get(url, headers=DEFAULT_REQUEST_HEADERS)
    # print(response.text)
    return response.text


def get_userHref(response):
    content = json.loads(response)
    for fans in content["fansList"]:
        uid = fans["uid"]
        yy = fans["yy"]
        nick = fans["nick"]
        logo = fans["logo"]
        sign = fans["sign"]
        logoIndex = fans["logoIndex"]
        pageurl = fans["pageurl"]
        diamondContribution = fans["diamondContribution"]
        signDate = fans["signDate"]
        v_type = fans["v_type"]
        entLevel = fans["entLevel"]
        type = fans["type"]
        title = fans["title"]
        sid = fans["sid"]
        subid = fans["subid"]
        pid = fans["pid"]
        liveurl = fans["liveurl"]
        persons = fans["persons"]
        fansPersons = fans["fansPersons"]
        hasfollowed = fans["hasfollowed"]
        date = fans["date"]
        print(uid, yy, nick, logo, sign, logoIndex, pageurl, diamondContribution, signDate, v_type, entLevel, type,
              title, sid, subid, pid, liveurl, persons, fansPersons, hasfollowed, date)









        # tree = etree.HTML(response)
        # href_list = tree.xpath('//a/@href')
        # for href in href_list:
        #     print(href)
        #     if "/U/" in href.upper():
        #         print(href)


if __name__ == "__main__":
    for i in range(1, 2428):
        url = "http://www.yy.com/u/follow/fans/1596032043?start={}&offset=20".format(i)
        # url = "http://www.yy.com/u/follow/1596032043#follow"
        try:
            print("URL = {}".format(url))
            print(get_response(url))
            # get_userHref(get_response(url))
        except Exception as e:
            print("ERROR:{}".format(e))
