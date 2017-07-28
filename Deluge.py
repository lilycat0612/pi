#coding=utf-8
__author__ = 'srv'
#!/usr/bin/python

from selenium import webdriver
import time
import os


dir=os.path.dirname(__file__)
chrome_driver_path=dir+"\chromedriver.exe"
print(dir)
browser=webdriver.Chrome(chrome_driver_path)
browser.get("http://192.168.1.104:8112/")
