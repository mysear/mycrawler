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

    #从scrapy框架继承，加入处理流程
    def parse(self, response):
        self.log('A response from %s just arrived!' % response.url)
        #i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        i = MyCrawlerItem()
        data = response.body
        soup = BeautifulSoup(data)

        for name in soup.find_all("div", class_="sp"):
            i["title"]=name.find("strong").a.string
            i["content"]=name.p.string
            i["link"]=name.find("strong").a['href']
            print ("content:",i["content"]," link:", i["link"], " title:",i["title"])
        return i

