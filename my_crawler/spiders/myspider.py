# -*- coding: utf-8 -*-
from __future__ import absolute_import
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from my_crawler.items import MyCrawlerItem
from bs4 import BeautifulSoup
from . import zhongyoo

class MySpider(CrawlSpider):
    name = 'myspider'
    allowed_domains = ['zhongyoo.com']
    start_urls = ['http://www.zhongyoo.com/name/']


    def parse_second_level(self, response):
        self.log('Second level response from %s just arrived!' % response.url)
        data = response.body

        if response.url.find("www.zhongyoo.com/name/page_"):
            pages = zhongyoo.parse_zhongyoo_page(data)
#            print("level 2 count:", len(pages))
            for i in range(0, len(pages)):
#                print(pages[i])
                yield scrapy.Request(pages[i], callback=self.parse_item)
        else:
            pass

    def parse_item(self, response):
        self.log('Parse item get response from %s just arrived!' % response.url)
        data = response.body
        if response.url.find("www.zhongyoo.com"):
            item = zhongyoo.parse_zhongyoo_item(data, response.url)
#            print(item)
            yield item
        else:
            pass

    #从scrapy框架继承，加入处理流程
    def parse(self, response):
        self.log('A response from %s just arrived!' % response.url)
        data = response.body

        if response.url.find("www.zhongyoo.com"):
            pages = zhongyoo.parse_zhongyoo(data)
            for i in range(0, len(pages)):
#                print(pages[i])
                yield scrapy.Request(pages[i], callback=self.parse_second_level)
        else:
            pass
