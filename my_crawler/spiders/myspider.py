# -*- coding: utf-8 -*-
from __future__ import absolute_import
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from my_crawler.items import MyCrawlerItem
from bs4 import BeautifulSoup
from . import zhongyoo
from . import zhongyaofang21nx

class MySpider(CrawlSpider):
    name = 'myspider'
    allowed_domains = ['zhongyoo.com', '21nx.com']
#    start_urls = ['http://www.zhongyoo.com/name/',
#                  'http://www.21nx.com/zhongyaofang/']
    start_urls = ['http://www.21nx.com/zhongyaofang/']

    def parse_second_level(self, response):
        self.log('Second level response from %s just arrived!' % response.url)
        data = response.body

        if response.url.find("www.zhongyoo.com/name/page_") != -1:
            pages = zhongyoo.parse_zhongyoo_page(data)
            for i in range(0, len(pages)):
                yield scrapy.Request(pages[i], callback=self.parse_item)
        elif response.url.find("http://www.21nx.com/zhongyaofang/index") != -1:
            pages = zhongyaofang21nx.parse_zhongyaofang21nx_page(data)
            for i in range(0, len(pages)):
                yield scrapy.Request(pages[i], callback=self.parse_item)
        else:
            pass

    def parse_item(self, response):
        self.log('Parse item get response from %s just arrived!' % response.url)
        data = response.body
        if response.url.find("www.zhongyoo.com") != -1:
            item = zhongyoo.parse_zhongyoo_item(data, response.url)
            yield item
        elif response.url.find("http://www.21nx.com/zhongyaofang") != -1:
            item = zhongyaofang21nx.parse_zhongyaofang21nx_item(data, response.url)
            yield item
#            pass
        else:
            pass

    #从scrapy框架继承，加入处理流程
    def parse(self, response):
        self.log('A response from %s just arrived!' % response.url)
        data = response.body

        if response.url.find("www.zhongyoo.com") != -1:
            pages = zhongyoo.parse_zhongyoo(data)
            for i in range(0, len(pages)):
                yield scrapy.Request(pages[i], callback=self.parse_second_level)
        elif response.url.find("www.21nx.com") != -1:
            pages = zhongyaofang21nx.parse_zhongyaofang21nx(data)
            for i in range(0, len(pages)):
#                print("Get url:", pages[i])
                yield scrapy.Request(pages[i], callback=self.parse_second_level)
        else:
            pass
