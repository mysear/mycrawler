# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from my_crawler.items import MyCrawlerItem
from bs4 import BeautifulSoup

class MySpider(CrawlSpider):
    name = 'myspider'
    allowed_domains = ['zhongyoo.com']
#    keyword="中药药材"
#    urlBaidu = "http://www.baidu.com/s?wd="+keyword
#    urlBaidu="http://www.zhongyoo.com/name/"
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

        print soup

    i["title"]=soup.title.string
    for link in soup.find_all('link'):
          i["link"]=link['href']
      break
    i["content"]=soup.title.string

    for string in soup.stripped_strings:
      print (repr(string))
    print "content:",i["content"]," link:", i["link"], " title:",i["title"]
        return i

