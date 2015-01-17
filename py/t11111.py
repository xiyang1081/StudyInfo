import urllib.request
url = "http://www.oschina.net/"
data = urllib.request.urlopen(url).read()
print data