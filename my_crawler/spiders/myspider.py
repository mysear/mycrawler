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

    def medicine_content(soupMedic):
         print(soupMedic)
         return 0

    def parse_item(self, response):
        data = response.body
        soup = BeautifulSoup(data, "lxml")
        i = MyCrawlerItem()

        conten_part = soup.find("div", class_="gaishu")
        i["title"] = conten_part.find("div", class_="title").h1.string
        i["link"] = ""
        i["content"] = ""

        print ("title:", i["title"])
        description = conten_part.find("div", class_="text")
        for content in description.find_all("p") :
            key = content.find("strong")
            if key == None:
              continue

            name = key.string
            if name == "中药名":
#                i["content"] = content.string
                print("medicine:", name)
            elif name == "别名":
#                i["link"] = content.string
                print("alias:", name)
            elif name == "英文名":
                 print("englishname:", name)
            elif name == "来源":
                 print("from:", name)
            elif name == "植物形态":
                 print("status:", name)
            elif name == "产地分布":
                 print("producing area:", name)
            elif name == "采收加工":
                 print("gather and reproduce:", name)
            elif name == "药材性状":
                 print("apperace:", name)
            elif name == "性味归经":
                 print("smell:", name)
            elif name == "功效与作用":
                 print("function:", name)
            elif name == "临床应用":
                 print("useage:", name)
            elif name == "药理研究":
                 print("research:", name)
            elif name == "化学成分":
                 print("chemical component:", name)
            elif name == "使用禁忌":
                 print("use forbidden:", name)
            elif name == "配伍药方":
                 print("prescription:", name)
#            else:
#                print ("others:", name)

        yield i


    #从scrapy框架继承，加入处理流程
    def parse(self, response):
        self.log('A response from %s just arrived!' % response.url)
        #i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        data = response.body
        soup = BeautifulSoup(data, "html5lib")

        for name in soup.find_all("div", class_="sp"):
#            i["title"]=name.find("strong").a.string
#            i["content"]=name.p.string
#            i["link"]=name.find("strong").a['href']
#            print ("content:",i["content"]," link:", i["link"], " title:",i["title"])
            url = name.find("strong").a['href']
            self.log('Acess url: %s' % url)
            yield scrapy.Request(url, callback=self.parse_item)
