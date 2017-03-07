#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    Author:cleverdeng
    E-mail:clverdeng@gmail.com
"""

#__version__ = '0.9'
#__all__ = ["PinYin"]

import os.path
#from . import word

word_dict = {}

def load_word():
    dict_file = os.getcwd() + '\my_crawler\spiders\word.data'
    if not os.path.exists(dict_file):
        raise IOError("NotFoundFile")

#    with file(dict_file) as f_obj:
    with open(dict_file) as f_obj:
        for f_line in f_obj.readlines():
            try:
                line = f_line.split('    ')
                word_dict[line[0]] = line[1]
            except:
                line = f_line.split('   ')
                word_dict[line[0]] = line[1]


def hanzi2pinyin(string=""):
    load_word()
    result = []
    if not isinstance(string, str):
        string = string.decode("utf-8")
    
#    for char in string:
#        key = '%X' % ord(char)
#        result.append(word_dict.get(key, char).split()[0][:-1].lower())
    for char in string:
        key = '%X' % ord(char)
        if not word_dict.get(key):
            result.append(char)
        else:
            result.append(word_dict.get(key, char).split()[0][:-1].lower())

    return result


def hanzi2pinyin_split(string="", split=""):
    result = hanzi2pinyin(string=string)
#    if split == "":
#        return result
#    else:
     return split.join(result)


#if __name__ == "__main__":
#    test = PinYin()
#    test.load_word()
#    string = "钓鱼岛是中国的"
#    print ("in: %s" % string)
#    print ("out: %s" % str(test.hanzi2pinyin(string=string)))
#   print ("out: %s" % test.hanzi2pinyin_split(string=string, split="-"))
