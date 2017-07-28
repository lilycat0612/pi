#coding=utf-8
__author__ = 'srv'
#!/usr/bin/python

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from smtplib import SMTPAuthenticationError

from selenium import webdriver
import time
import os

from pyquery import PyQuery

url='http://ipaddress.com/'

#hard code need to changed
username = 'rpi_report_ip@outlook.com'  # Email Address from the email you want to send an email
password = 'ThisIsRobot'  # Password
server = smtplib.SMTP('')
from_addr='rpi_report_ip@outlook.com'

"""
SMTP Server Information
1. Gmail.com: smtp.gmail.com:587
2. Outlook.com: smtp-mail.outlook.com:587
3. Office 365: outlook.office365.com
Please verify your SMTP settings info.
"""

# Create the body of the message (a HTML version for formatting).
html = """Add you email body here"""


# Function that send email.
def send_mail(username, password, from_addr, to_addrs, msg):
    #server = smtplib.SMTP('smtp-mail.outlook.com', '587')
    server = smtplib.SMTP('Smtp.live.com', '25')#hard code need to changed
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username, password)
    server.sendmail(from_addr, to_addrs, msg.as_string())
    server.quit()

# find by selenium
# dir=os.path.dirname(__file__)
# chrome_driver_path=dir+"\chromedriver.exe"
# browser=webdriver.Chrome(chrome_driver_path)
# browser.get("https://www.whatismyip.com/ip-address-lookup/")

# MyIP=browser.find_element_by_name("ip").get_attribute("value")
# print(MyIP)
# browser.close()

#find by PyQuery
page_date=PyQuery(url)
MyIP=page_date('.navbar-text.navbar-right').text()

#write my IP to the file
file_object = open('C:/workspace/selenium/src/pi/IP.txt', 'r')#hard code need to changed
old_IP = file_object.read()
if MyIP==old_IP:
    print('The IP does NOT change')
    file_object.close()
    
else:#if the IP address changed to write it down and send email 
    print('The IP DO change')
    file_object = open('C:/workspace/selenium/src/pi/IP.txt', 'w')#hard code need to changed
    file_object.write(MyIP)
    file_object.close()
    # Read to_addrs email list txt
    #email_list = [line.strip() for line in open('/home/pi/python_code/email.txt')] #for linux
    email_list = [line.strip() for line in open('C:/workspace/selenium/src/pi/email.txt')] #for windows #hard code need to changed

    for to_addrs in email_list:
        msg = MIMEMultipart()
        msg['Subject'] = "You IP address has changed" + MyIP
        msg['From'] = from_addr
        msg['To'] = to_addrs

        # Attach HTML to the email
        #body = MIMEText(html, 'html')
        #msg.attach(body)

        # Attach Cover Letter to the email
        #cover_letter = MIMEApplication(open("file1.pdf", "rb").read())
        #cover_letter.add_header('Content-Disposition', 'attachment', filename="file1.pdf")
        #msg.attach(cover_letter)

        # Attach Resume to the email
        #cover_letter = MIMEApplication(open("file2.pdf", "rb").read())
        #cover_letter.add_header('Content-Disposition', 'attachment', filename="file2.pdf")
        #msg.attach(cover_letter)

        try:
            send_mail(username, password, from_addr, to_addrs, msg)
            print ("Email successfully sent to")+to_addrs
        #The sever doesn't accept username and password
        except SMTPAuthenticationError:
            print ('SMTPAuthenticationError')
            print ("Email not sent to")+to_addrs









