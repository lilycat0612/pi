#!python
# encoding: utf-8
from urllib import request
from urllib import parse
from pyquery import PyQuery as pq

DEFAULT_HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0"}
DEFAULT_TIMEOUT = 120


def get(url):
    req = request.Request(url, headers=DEFAULT_HEADERS)
    response = request.urlopen(req, timeout=DEFAULT_TIMEOUT)
    content = ""
    if response:
        content = response.read().decode("utf8","ignore")
        response.close()
    return content


def post(url, **paras):
    param = parse.urlencode(paras).encode("utf8","ignore")
    req = request.Request(url, param, headers=DEFAULT_HEADERS)
    response = request.urlopen(req, timeout=DEFAULT_TIMEOUT)
    content = ""
    if response:
        content = response.read().decode("utf8","ignore")
        response.close()
    return content


def main():
    url = "https://www.torrentkitty.tv/search/"

    get_content = post(url, q=parse.quote("蝙蝠侠"))
    print(get_content)
    get_content = get(url)
    print(get_content)
    


  

    

if __name__ == "__main__":
    main()