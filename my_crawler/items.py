# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class MyCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    namePin = scrapy.Field()
    nameCh = scrapy.Field()
    alias = scrapy.Field()
    nameEng = scrapy.Field()
    source = scrapy.Field()
    description = scrapy.Field()
    area = scrapy.Field()
    gather = scrapy.Field()
    shape = scrapy.Field()
    taste = scrapy.Field()
    effect = scrapy.Field()
    application = scrapy.Field()
    pharmacology = scrapy.Field()
    component = scrapy.Field()
    tatoo = scrapy.Field()
    prescription = scrapy.Field()
    url = scrapy.Field()
    pass
