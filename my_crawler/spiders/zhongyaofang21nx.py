# -*- coding: utf-8 -*-
from __future__ import absolute_import
import unicodedata
from bs4 import BeautifulSoup
from my_crawler.items import MyCrawlerItem
from . import pinyin

def parse_zhongyaofang21nx(data):
    soup = BeautifulSoup(data, "html5lib")

    pageList = []
    for page in soup.find("div", class_="qq").find("div", class_="Q1").find("div", class_="Lbt").find_all("a"):
        urlReq="www.21nx.com/zhongyaofang/" + page.get('href').get_text()
        print(urlReq)
        pageList.append(urlReq)
    return pageList

def parse_zhongyaofang21nx_page(data):
    soup = BeautifulSoup(data, "html5lib")
    pageInfo = soup.find("div", class_="qq").find("div", class_="Q1").find("ul", class_="U4").find_all("li")
    pageList = []
    for name in pageInfo:
        urlReq = "www.21nx.com/zhongyaofang/" + name.a['href']
        print(urlReq)
        pageList.append(urlReq)
    return pageList

def parse_zhongyaofang21nx_item(data, urlReq):
    print("Get resp from:", urlReq)
    soup = BeautifulSoup(data, "html5lib")
    item = MyCrawlerItem()
    item['nameCh'] = ""
    item['namePin'] = ""
    item['alias'] = ""
    item['nameEng'] = ""
    item['source'] = ""
    item['description'] = ""
    item['area'] = ""
    item['gather'] = ""
    item['shape'] = ""
    item['taste'] = ""
    item['effect'] = ""
    item['application'] = ""
    item['pharmacology'] = ""
    item['component'] = ""
    item['tatoo'] = ""
    item['prescription'] = ""
    item['url'] = urlReq

    conten_part = soup.find("div", class_="gaishu")
    if conten_part == None:
        return

    return