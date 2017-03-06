# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from my_crawler.items import MyCrawlerItem
from bs4 import BeautifulSoup

class MySpider(CrawlSpider):
    name = 'myspider'
    allowed_domains = ['zhongyoo.com']
    start_urls = ['http://www.zhongyoo.com/name/']


    def parse_item(self, response):
        data = response.body
        soup = BeautifulSoup(data, "html5lib")
        item = MyCrawlerItem()
        item['nameCh'] = ""
        item['namePin'] = ""
        item['alias'] = ""
        item['nameEng'] = ""
        item['source'] = ""
        item['description'] = ""
        item['area'] = ""
        item['gather'] = ""
        item['shape'] = ""
        item['taste'] = ""
        item['effect'] = ""
        item['application'] = ""
        item['pharmacology'] = ""
        item['component'] = ""
        item['tatoo'] = ""
        item['prescription'] = ""

        conten_part = soup.find("div", class_="gaishu")
        if conten_part == None:
          return
        description = conten_part.find("div", class_="text")
        print ("text:", description)
        for content in description.find_all("p") :
            if content == None:
              continue
            else:
              key = content.find("strong")
              if key == None:
                continue

#            print ("所有内容:", content)
            str = ""
            str = content.get_text().strip()
            strCont = str[str.find("】") + 1:].strip()
            name = key.string
            if name == "中药名":
                [nameCh, namePin] = strCont.split(' ')
                item['nameCh'] = nameCh.strip()
                item['namePin'] = namePin.strip()
#                print("++++++++++中药名:", item['nameCh'], item['namePin'])
            elif name == "别名":
                item['alias'] = strCont
#                print("++++++++++别名:", item['alias'])
            elif name == "英文名":
                item['nameEng'] = strCont
#                print("++++++++++英文名:", item['nameEng'])
            elif name == "来源":
                item['source'] = strCont
#                print("++++++++++来源:", item['source'])
            elif name == "植物形态":
                item['description'] = strCont
#                print("++++++++++植物形态:", item['description'])
            elif name == "产地分布":
                item['area'] = strCont
#                print("++++++++++产地分布:", item['area'])
            elif name == "采收加工":
                item['gather'] = strCont
#                print("++++++++++采收加工:", item['gather'])
            elif name == "药材性状":
                item['shape'] = strCont
#                print("++++++++++药材性状:", item['shape'])
            elif name == "性味归经":
                item['taste'] = strCont
#                print("++++++++++性味归经:", item['taste'])
            elif name == "功效与作用":
                item['effect'] = strCont
#                print("++++++++++功效与作用:", item['effect'])
            elif name == "临床应用":
                item['application'] = strCont
#                print("++++++++++临床应用:", item['application'])
            elif name == "药理研究":
                item['pharmacology'] = strCont
#                print("++++++++++药理研究:", item['pharmacology'])
            elif name == "化学成分":
                item['component'] = strCont
#                print("++++++++++化学成分:", item['component'])
            elif name == "使用禁忌":
                item['tatoo'] = strCont
#                print("++++++++++使用禁忌:", item['tatoo'])
            elif name == "配伍药方" or name == "相关药方":
                item['prescription'] = strCont
#                print("++++++++++配伍药方:", item['prescription'])
#            else:
#                print ("others:", name)
        yield item

    def parse_zhongyao(self, response):
      data = response.body
      soup = BeautifulSoup(data, "html5lib")

      for name in soup.find_all("div", class_="sp"):
        url = name.find("strong").a['href']
        self.log('Acess url: %s' % url)
        yield scrapy.Request(url, callback=self.parse_item)

    #从scrapy框架继承，加入处理流程
    def parse(self, response):
        self.log('A response from %s just arrived!' % response.url)

        data = response.body
        soup = BeautifulSoup(data, "html5lib")

        pageInfo = soup.find("ul", class_="pagelist").find("span", class_="pageinfo").get_text()
        lastPage = int(pageInfo[pageInfo.find("共")+1:pageInfo.find("页")])
        for i in range(1, lastPage + 1):
          urlReq="http://www.zhongyoo.com/name/page_" + str(i) + ".html"
          yield scrapy.Request(urlReq, callback=self.parse_zhongyao)
