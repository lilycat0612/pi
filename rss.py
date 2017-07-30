#coding=utf-8
from pyquery import PyQuery
import urllib
url='http://www.ttmeiju.com/index.php/user/myrss.html'

d=PyQuery(url)
print(d)
b=d(".contextbox").text()
#c=b('.a').attr('href')
#a=d('head').html()
#a=d('.navbar-text.navbar-right').text()
#.encode('utf-8')
print(b)
#print(c)