#coding=utf-8
from xml.parsers.expat import ParserCreate
import urllib
import json

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        if name=='yweather:forecast':
            print '日期：',attrs[u'date'],'天气：',attrs[u'text'],'最高气温:',attrs[u'high'],'摄氏度','最低气温：',attrs[u'low'],'摄氏度','星期：',attrs[u'day']
    def end_element(self, name):
        pass
        """
        if name=='yweather:forecast':
            print('sax:end_element: %s' % name)
            """
    def char_data(self, text):
        pass
        #print('sax:char_data: %s' % text)

html=urllib.urlopen('http://weather.yahooapis.com/forecastrss?u=c&w=2151330')
xml=html.read()
#print 'xml:',xml
"""

xml = r'''
<rss xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#" version="2.0">
<yweather:forecast day="Wed" date="10 Dec 2014" low="-6" high="5" text="Sunny/Wind" code="24"/>
<yweather:forecast day="Thu" date="11 Dec 2014" low="-6" high="3" text="Sunny" code="32"/>
<yweather:forecast day="Fri" date="12 Dec 2014" low="-8" high="4" text="Sunny" code="32"/>
<yweather:forecast day="Sat" date="13 Dec 2014" low="-8" high="3" text="Sunny" code="32"/>
<yweather:forecast day="Sun" date="14 Dec 2014" low="-4" high="3" text="Mostly Sunny" code="34"/>
'''
"""
handler = DefaultSaxHandler()
parser = ParserCreate()
parser.returns_unicode = True
parser.StartElementHandler = handler.start_element
#parser.EndElementHandler = handler.end_element
#parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)
