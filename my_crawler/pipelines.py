# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import pymysql.cursors
import time

class MyCrawlerPipeline(object):
    def exeSQL(self, sql):
        '''
        功能：连接MySQL数据库并执行sql语句
        @sql：定义SQL语句
        '''
        con = pymysql.connect(
            host='localhost',
            user='root',
            passwd='root',
            db='scrawler',
            charset='utf8',
            )
        cur =con.cursor()
        cur.execute(sql)
        con.commit()
        con.close()
    def process_item(self, item, spider):
        namePin = item['namePin']
        nameCh = item['nameCh']
        nameEng = item['nameEng']
        alias = item['alias']
        source = item['source']
        description = item['description']
        area = item['area']
        gather = item['gather']
        shape = item['shape']
        taste = item['taste']
        effect = item['effect']
        application = item['application']
        pharmacology = item['pharmacology']
        component = item['component']
        tatoo = item['tatoo']
        prescription = item['prescription']

        try:
           sql= "insert into myspider(namePin, nameCh, nameEng, alias, source, description, area, gather, \
                shape, taste, effect, application, pharmacology, component, tatoo, prescription) \
                values('"+namePin+"','"+nameCh+"','"+nameEng+"','"+alias+"','"+source+"', \
                '"+description+"','"+area+"','"+gather+"','"+shape+"','"+taste+"','"+effect+"', \
                '"+application+"','"+pharmacology+"','"+component+"','"+tatoo+"','"+prescription+"')"
           self.exeSQL(sql)
        except Exception as er:
           print("插入错误，错误如下：")
           print(er)

        return item