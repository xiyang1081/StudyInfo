#coding=utf-8
from xml.parsers.expat import ParserCreate
import urllib


class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        if name=='yweather:forecast':
            print '日期：',attrs[u'date'],'天气：',attrs[u'text'],'最高气温:',attrs[u'high'],'摄氏度','最低气温：',attrs[u'low'],'摄氏度','星期：',attrs[u'day']

if __name__=='__main__':
    html=urllib.urlopen('http://weather.yahooapis.com/forecastrss?u=c&w=2151330')
    xml=html.read()
    #print 'xml:',xml
    handler = DefaultSaxHandler()
    parser = ParserCreate()
    #parser.returns_unicode = True
    parser.StartElementHandler = handler.start_element
    parser.Parse(xml)
