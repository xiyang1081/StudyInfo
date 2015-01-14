#-*- coding: cp936 -*-
import re
import string

common_used_numerals_tmp ={'��':0, 'һ':1, '��':2, '��':2, '��':3, '��':4, '��':5, '��':6, '��':7, '��':8, '��':9, 'ʮ':10, '��':100, 'ǧ':1000, '��':10000, '��':100000000}
common_used_numerals = {}
for key in common_used_numerals_tmp:
    common_used_numerals[key.decode('cp936')] = common_used_numerals_tmp[key]

def chinese2digits(uchars_chinese):
    total = 0
    r = 1                           #��ʾ��λ����ʮ��ǧ...
    for i in range(len(uchars_chinese) - 1, -1, -1):
        val = common_used_numerals.get(uchars_chinese[i])
        if val >= 10 and i == 0:    #Ӧ�� ʮ�� ʮ�� ʮ*֮��
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


print chinese2digits('������ʮ��'.decode('cp936'))
print "-------------------------"
print chinese2digits('ʮ��'.decode('cp936'))
print "-------------------------"
print chinese2digits('һ������������ٶ�ʮ��'.decode('cp936'))
