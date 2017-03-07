# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from my_crawler.items import MyCrawlerItem

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

def parse_zhongyoo_item(data):
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

    conten_part = soup.find("div", class_="gaishu")
    if conten_part == None:
      return

    description = conten_part.find("div", class_="text")
#    print ("text:", description)
    for content in description.find_all("p") :
      if content == None:
        continue
      else:
        key = content.find("strong")
        if key == None:
          continue

#      print ("所有内容:", content)
      str = ""
      str = content.get_text().strip()
      strCont = str[str.find("】") + 1:].strip()
      name = key.string
      #关键字为"药名"或"中药名"
      if name.find("药名") != -1:
#       [nameCh, namePin] = strCont.split(' ')
        strCont.replace('；','')
        print(content)
        print(content.get_text())
        if strCont.find(' ') == -1:
            item['nameCh'] = strCont.strip()
        else:
            item['nameCh'] = strCont[:strCont.find(' ')].strip()
            item['namePin'] = strCont[strCont.find(' ')+1:].strip()
        print("++++++++++中药名:", item['nameCh'], item['namePin'])
      elif name.find("别名") != -1:
        item['alias'] = strCont
#         print("++++++++++别名:", item['alias'])
      elif name.find("英文名") != -1:
        item['nameEng'] = strCont
#        print("++++++++++英文名:", item['nameEng'])
      elif name.find("来源") != -1:
        item['source'] = strCont
#        print("++++++++++来源:", item['source'])
      elif name.find("植物形态") != -1:
        item['description'] = strCont
#        print("++++++++++植物形态:", item['description'])
      #键字为"产地分布"或"生境分布"
      elif name.find("分布") != -1:
        item['area'] = strCont
#        print("++++++++++产地分布:", item['area'])
      elif name.find("采收加工") != -1:
        item['gather'] = strCont
#        print("++++++++++采收加工:", item['gather'])
      elif name.find("药材性状") != -1:
        item['shape'] = strCont
#        print("++++++++++药材性状:", item['shape'])
      elif name.find("性味归经") != -1:
        item['taste'] = strCont
#        print("++++++++++性味归经:", item['taste'])
      elif name.find("功效与作用") != -1:
        item['effect'] = strCont
#        print("++++++++++功效与作用:", item['effect'])
      elif name.find("临床应用") != -1:
        item['application'] = strCont
#        print("++++++++++临床应用:", item['application'])
      elif name.find("药理研究") != -1:
        item['pharmacology'] = strCont
#        print("++++++++++药理研究:", item['pharmacology'])
      #关键字为"化学成分"或"主要成分"
      elif name.find("成分") != -1:
        print(content.get_text())
        strCont.replace('；','')
        item['component'] = strCont
        print("++++++++++化学成分:", item['component'])
      elif name.find("使用禁忌") != -1:
        item['tatoo'] = strCont
#        print("++++++++++使用禁忌:", item['tatoo'])
      #关键字为"配伍药方"或"相关药方"
      elif name.find("药方") != -1:
        item['prescription'] = strCont
#        print("++++++++++配伍药方:", item['prescription'])
      else:
#        print ("others:", name)
        pass
#end of for()

    return item