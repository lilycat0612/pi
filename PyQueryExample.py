

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
                Cool!
            </div>
            <li>list2</li>
        </ul>
    </body>
</html>
'''

doc = pyq(html)

print doc('title') # 获取 title 标签的源码
# <title>这是标题</title>

print doc('title').text() # 获取 title 标签的内容
# 这是标题

print doc('.ha').text() # 获取 class 为 ha 的标签的内容
# Cool!

print doc('#hi').text() # 获取 id 为 hi 的标签的内容
# Hello

print doc('p:first').text() # 还可以支持伪类

li = doc('li') # 处理多个元素
for i in li:
    print pyq(i).text()