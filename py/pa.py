#coding=utf-8
import re
import sys
import mechanize
import cookielib
from  bs4 import BeautifulSoup

br = mechanize.Browser()        ##建立浏览器对象
cj = cookielib.LWPCookieJar()   ##通过导入cookielib模块，并设置浏览器cookie，可以在需要认证的网络行为之后不用重复认证登陆
br.set_cookiejar(cj)        ##关联cookies  


###设置一些参数，因为是模拟客户端请求，所以要支持客户端的一些常用功能，比如gzip,referer等
br.set_handle_equiv(True) 
br.set_handle_gzip(True) 
br.set_handle_redirect(True) 
br.set_handle_referer(True) 
br.set_handle_robots(False) 


###这个是degbug##你可以看到他中间的执行过程，对调试代码有帮助 
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.set_debug_http(True) 
br.set_debug_redirects(True) 
br.set_debug_responses(True) 
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
