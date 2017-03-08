# -*- coding: utf-8 -*-
from __future__ import absolute_import
from bs4 import BeautifulSoup
from my_crawler.items import MyCrawlerItem
from . import pinyin

def parse_zhongyoo(data):
    soup = BeautifulSoup(data, "html5lib")
    pageInfo = soup.find("ul", class_="pagelist").find("span", class_="pageinfo").get_text()
    lastPage = int(pageInfo[pageInfo.find("共")+1:pageInfo.find("页")])
    print("一共有",lastPage,"页信息");

    pageList = []
    for i in range(1, lastPage + 1):
      urlReq="http://www.zhongyoo.com/name/page_" + str(i) + ".html"
      pageList.append("http://www.zhongyoo.com/name/page_" + str(i) + ".html")
    return pageList

def parse_zhongyoo_page(data):
    soup = BeautifulSoup(data, "html5lib")

    pageList = []
    for name in soup.find_all("div", class_="sp"):
      url = name.find("strong").a['href']
      pageList.append(url)
    return pageList

def parse_zhongyoo_item(data, url):
    print("Get resp from:", url)
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
    item['url'] = url

    conten_part = soup.find("div", class_="gaishu")
    if conten_part == None:
#      print("No find gaishu in ", url)
      return

    aliasFlag = False
    description = conten_part.find("div", class_="text")
#    print ("find text in ", url)
    for content in description.find_all("p") :
      if content == None:
        continue
      else:
        key = content.find("strong")
        if key == None:
          continue

      strTmp = ""
      strTmp = content.get_text().strip()
      strCont = strTmp[strTmp.find("】") + 1:].strip()
      name = key.string
      #关键字为"药名"或"中药名"
      if name.find("药名") != -1 or name.find("中药名") != -1:
        print(content.get_text())
        strCont = strCont.replace('；','').replace('’','').replace('\'','')
        if strCont.find(' ') == -1:
            item['nameCh'] = strCont.strip()
            item['namePin'] = pinyin.hanzi2pinyin(string=item['nameCh'])
        else:
            item['nameCh'] = strCont[:strCont.find(' ')].strip()
            item['namePin'] = pinyin.yinfu2pinyin(string=strCont[strCont.find(' ')+1:].strip().replace(' ',''))
        #直接汉字转拼音，不再使用获取到的拼音，可能有误
#        if strCont.find(' ') == -1:
#          item['nameCh'] = strCont.strip()
#        else:
#          item['nameCh'] = strCont[:strCont.find(' ')].strip()
#        item['namePin'] = pinyin.hanzi2pinyin(string=item['nameCh'])
#        print("++++++++++中药名:", item['nameCh'], item['namePin'])
      #有英文名写成别名的，判断是否已经获取过别名，如果获取过当前即为英文名
      elif name.find("别名") != -1:
        if aliasFlag == False:
          print(content.get_text())
          item['alias'] = strCont
          aliasFlag = True
          print("alias:", item['alias'])
        else:
          item['nameEng'] = strCont.replace('；','').replace('’','').replace('\'','')
          print("Englishname:", item['nameEng'])
#         print("++++++++++别名:", item['alias'])
      elif name.find("英文名") != -1:
        print(content.get_text())
        item['nameEng'] = strCont.replace('；','').replace('’','').replace('\'','')
#        print("++++++++++英文名:", item['nameEng'])
      elif name.find("来源") != -1:
        item['source'] = strCont.replace(';','').replace('\'','')
#        print("++++++++++来源:", item['source'])
      elif name.find("植物形态") != -1:
        item['description'] = strCont.replace(';','').replace('\'','')
#        print("++++++++++植物形态:", item['description'])
      #键字为"产地分布"或"生境分布"
      elif name.find("产地分布") != -1 or name.find("生境分布") != -1:
        item['area'] = strCont.replace(';','').replace('\'','')
#        print("++++++++++产地分布:", item['area'])
      elif name.find("采收加工") != -1:
        item['gather'] = strCont.replace(';','').replace('\'','')
#        print("++++++++++采收加工:", item['gather'])
      elif name.find("药材性状") != -1:
        item['shape'] = strCont.replace(';','').replace('\'','')
#        print("++++++++++药材性状:", item['shape'])
      elif name.find("性味归经") != -1:
        item['taste'] = strCont.replace(';','').replace('\'','')
#        print("++++++++++性味归经:", item['taste'])
      elif name.find("功效与作用") != -1:
        item['effect'] = strCont.replace(';','').replace('\'','')
#        print("++++++++++功效与作用:", item['effect'])
      elif name.find("临床应用") != -1:
        item['application'] = strCont.replace(';','').replace('\'','')
#        print("++++++++++临床应用:", item['application'])
      elif name.find("药理研究") != -1:
        item['pharmacology'] = strCont.replace(';','').replace('\'','')
#        print("++++++++++药理研究:", item['pharmacology'])
      #关键字为"化学成分"或"主要成分"
      elif name.find("化学成分") != -1 or name.find("主要成分") != -1:
#        print("Ori:",content.get_text())
#        print("Handle:",strCont.replace(';','').replace('\'',''))
        item['component'] = strCont.replace(';','').replace('\'','').replace('₁','1').replace('₃','3')
#        print("++++++++++化学成分:", item['component'])
      elif name.find("使用禁忌") != -1:
        item['tatoo'] = strCont.replace(';','').replace('\'','')
#        print("++++++++++使用禁忌:", item['tatoo'])
      #关键字为"配伍药方"或"相关药方"
      elif name.find("配伍药方") != -1 or name.find("相关药方") != -1:
        for tagP in content.find_next_siblings("p"):
          strTag = tagP.get_text().strip()
          if strTag == "" or strTag.find("相关推荐文章") != -1:
            break
          else:
            strCont = strCont + strTag
        item['prescription'] = strCont.replace(';','').replace('\'','')
#        print("++++++++++配伍药方:", item['prescription'])
      else:
        pass
#end of for()

    return item
