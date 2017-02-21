# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
import time

class MyCrawlerPipeline(object):

    def exeSQL(self, sql):
        '''
        功能：连接MySQL数据库并执行sql语句
        @sql：定义SQL语句
        '''
        con = MySQLdb.connect(
            host='localhost',
            user='root',
            passwd='root',
            db='scrawler',
            charset='utf8',
            local_infile=1
            )
        con.query(sql)
        con.commit()
        con.close()
    def process_item(self, item, spider):
        link_url = item['link'].decode('utf8')
        content_header = item['content']
        if (len(link_url) and len(content_header)):#判断是否为空值
            try:
               content_header = MySQLdb.escape_string(content_header)
               link_url = MySQLdb.escape_string(link_url)
               print("cotent:%s link:%s" % (content_header,link_url))
               sql="insert into myspider(content,link) values('"+content_header+"','"+link_url+"')"
               self.exeSQL(sql)
            except Exception as er:
               print("插入错误，错误如下：")
               print(er)
        else:
            pass
        return item