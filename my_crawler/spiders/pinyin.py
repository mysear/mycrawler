#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    Author:cleverdeng
    E-mail:clverdeng@gmail.com
"""

#__version__ = '0.9'
#__all__ = ["PinYin"]

import os.path
import sys
import unicodedata

word_dict = {}

def search_file(inputname, search_path=os.environ['PATH'], pathsep=os.pathsep):
    for parent,dirnames,filenames in os.walk(search_path):
        for filename in filenames:
            if filename == inputname:
                fullpath = os.path.join(parent, inputname)
                return fullpath
        for dirname in dirnames:
            res = search_file(inputname, dirname)
            if res != None:
               return res

def load_word():
    dict_file = 'word.data'
    file_path = search_file(dict_file, os.getcwd())
    print(file_path, os.getcwd())
    if not os.path.exists(file_path):
        raise IOError("NotFoundFile")

#    with file(file_path) as f_obj:
    with open(file_path) as f_obj:
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

def yinfu2pinyin(string=''):
    '''
    通过使用dict.fromkeys() 方法构造一个字典，每个Unicode 和音符作为键，对于的值全部为None
    然后使用unicodedata.normalize() 将原始输入标准化为分解形式字符
    sys.maxunicode : 给出最大Unicode代码点的值的整数，即1114111（十六进制的0x10FFFF）。
    unicodedata.combining:将分配给字符chr的规范组合类作为整数返回。 如果未定义组合类，则返回0。
    '''
    newStr = ""
    if 2 == sys.version_info[0]:
      cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(unichr(c)))
      newStr = unicodedata.normalize('NFD', string.decode('utf-8'))
    else:
      cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
      newStr = unicodedata.normalize('NFD', string)
    newStr = newStr.translate(cmb_chrs)
    return newStr

#if __name__ == "__main__":
#    test = PinYin()
#    test.load_word()
#    string = "钓鱼岛是中国的"
#    print ("in: %s" % string)
#    print ("out: %s" % str(test.hanzi2pinyin(string=string)))
#   print ("out: %s" % test.hanzi2pinyin_split(string=string, split="-"))
