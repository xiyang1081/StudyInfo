#!/usr/bin/env python
#coding=utf-8
'''
读取*.ini文件
'''
import ConfigParser


config = ConfigParser.ConfigParser()
config.read('boot.ini')
sections=config.sections()
print '配置块：',sections
for op in sections:
    o=config.options(op)
    print 'option:',o
    for i in o:
        a=config.get(op,i)
        print a
