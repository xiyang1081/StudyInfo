import urllib
import urllib2

url='http://www.zte.com.cn/cn/'

user_agent='Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'
values={'name':'WHY','location':'SDU','language':'Python'}
headers={'User-Agent':user_agent}

data=urllib.urlencode(values)

req=urllib.Request(url,data,headers)
response=urllib2.urlopen(req)

the_page=response.read()


print the_page
