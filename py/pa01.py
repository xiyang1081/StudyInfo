import urllib2

res=urllib2.urlopen('http://image.baidu.com/i?tn=baiduimage&ct=201326592&lm=-1&cl=2&word=%CB%D1%B9%B7%D7%C0%C3%E6%B1%DA%D6%BD&fr=ala1')
html=res.read()
print html
