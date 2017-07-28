#coding=utf-8
from pyquery import PyQuery
url='http://ipaddress.com/'


#print doc('.ha').text() # 获取 class 为 ha 的标签的内容
d=PyQuery('<body class="container"><div class="ad mobile top"><script>(adsbygoogle = window.adsbygoogle || []).push({});</script></div><h1>Your IP address is: 175.163.245.87</h1></body>')
d=PyQuery(url)

a=d('.container').text().encode('utf-8')
#a=d('.navbar-text.navbar-right').text()
#.encode('utf-8')
print(a)

#print(d)




#print(d('.ad.mobile.top').text())


#!/usr/bin/python
# -*- coding: UTF-8 -*-

from pyquery import PyQuery as pyq


html = '''
<html>
    <head>
        <title>这是标题</title>
    </head>
    <body>
        <p id="hi">Hello</p>
        <ul>
            <li>list1</li>
            <div class="ha">
                <h1>Cool!</hi>
            </div>
            <li>list2</li>
        </ul>
    </body>
</html>
'''

doc = pyq(html)


print (doc('title').text()) # 获取 title 标签的内容
# 这是标题

print (doc('.ha').text()) # 获取 class 为 ha 的标签的内容
# Cool!

print (doc('#hi').text()) # 获取 id 为 hi 的标签的内容
# Hello

