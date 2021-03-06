#-*- coding: cp936 -*-
import re
import string

common_used_numerals_tmp ={'零':0, '一':1, '二':2, '两':2, '三':3, '四':4, '五':5, '六':6, '七':7, '八':8, '九':9, '十':10, '百':100, '千':1000, '万':10000, '亿':100000000}
common_used_numerals = {}
for key in common_used_numerals_tmp:
    common_used_numerals[key.decode('cp936')] = common_used_numerals_tmp[key]

def chinese2digits(uchars_chinese):
    total = 0
    r = 1                           #表示单位：个十百千...
    for i in range(len(uchars_chinese) - 1, -1, -1):
        val = common_used_numerals.get(uchars_chinese[i])
        if val >= 10 and i == 0:    #应对 十三 十四 十*之类
            if val > r:
                r = val
                total = total +  val
            else:
                r = r * val
                #total =total +  r * x 
        elif val >= 10:
            if val > r:
                r = val
            else:
                r = r * val
        else:
            total = total +  r * val
    
    return total


print chinese2digits('两百三十二'.decode('cp936'))
print "-------------------------"
print chinese2digits('十二'.decode('cp936'))
print "-------------------------"
print chinese2digits('一亿零八万零三百二十三'.decode('cp936'))
