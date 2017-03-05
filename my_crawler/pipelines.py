# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#import MySQLdb
import pymysql
import pymysql.cursors
import time

class MyCrawlerPipeline(object):
#    pass
    def exeSQL(self, sql):
        '''
        功能：连接MySQL数据库并执行sql语句
        @sql：定义SQL语句
        '''
#        con = MySQLdb.connect(
        con = pymysql.connect(
            host='localhost',
            user='root',
            passwd='root',
            db='scrawler',
            charset='utf8',
#            port = 3307
#            local_infile=1
            )
        cur =con.cursor()
        cur.execute(sql)
#        con.query(sql)
        con.commit()
        con.close()
    def process_item(self, item, spider):
#        link_url = item['link'].decode('utf8')
        namePin = item['namePin']
        nameCh = item['nameCh']
        nameEng = item['nameEng']
#        print("#######################药材:", namePin, nameCh, nameEng)
        alias = item['alias']
#        print("#######################alias:", alias, item['alias'])
        source = item['source']
#        print("#######################source:", source, item['source'])
        description = item['description']
#        print("#######################description:", description, item['description'])
        area = item['area']
#        print("#######################area:", area, item['area'])
        gather = item['gather']
#        print("#######################gather:", gather, item['gather'])
        shape = item['shape']
#        print("#######################shape:", shape, item['shape'])
        taste = item['taste']
#        print("#######################taste:", taste, item['taste'])
        effect = item['effect']
#        print("#######################effect:", effect, item['effect'])
        application = item['application']
#        print("#######################application:", application, item['application'])
        pharmacology = item['pharmacology']
#        print("#######################pharmacology:", pharmacology, item['pharmacology'])
        component = item['component']
#        print("#######################component:", component, item['component'])
        tatoo = item['tatoo']
#        print("#######################tatoo:", tatoo, item['tatoo'])
        prescription = item['prescription']
#        print("#######################prescription:", prescription, item['prescription'])

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
#        else:
#            pass
        return item