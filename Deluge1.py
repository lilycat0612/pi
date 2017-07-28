#coding=utf-8
__author__ = 'srv'
#!/usr/bin/python

from selenium import webdriver
import os

browser=webdriver.Chrome(os.path.expanduser("/usr/lib/chromium-browser/chromedriver"))
browser.get("http://localhost:8112/")
