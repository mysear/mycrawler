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
        print ("content:", conten_part)
#        i["title"] = conten_part.find("div", class_="title").h1.string
#        print ("title:", i["title"])
#        description = conten_part.find("div", class_="text")
#        for content in description.find_all("p") :
#            name = content.strong.string
#            if name == "中药名":
#                print("中药名：", name)
#            elif name == "别名":
#                print("别名：", name)
#            else:
#                print ("name:", name)

        yield i


    #从scrapy框架继承，加入处理流程
    def parse(self, response):
        self.log('A response from %s just arrived!' % response.url)
        #i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        data = response.body
        soup = BeautifulSoup(data)

        for name in soup.find_all("div", class_="sp"):
#            i["title"]=name.find("strong").a.string
#            i["content"]=name.p.string
#            i["link"]=name.find("strong").a['href']
#            print ("content:",i["content"]," link:", i["link"], " title:",i["title"])
            url = name.find("strong").a['href']
            self.log('Acess url: %s' % url)
            yield scrapy.Request(url, callback=self.parse_item)

