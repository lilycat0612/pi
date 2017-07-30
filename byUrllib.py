import urllib
from urllib import request
url='http://ipaddress.com/'
url='https://www.baidu.com/'

page=urllib.request.urlopen(url)

print(page.read())