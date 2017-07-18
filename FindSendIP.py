#coding=utf-8
__author__ = 'srv'
#!/usr/bin/python

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from smtplib import SMTPAuthenticationError
from smtplib import SMTPHeloError
from smtplib import SMTPRecipientsRefused
from smtplib import SMTPSenderRefused
from smtplib import SMTPDataError
from selenium import webdriver
import time
import os
import unittest

class FindMyIP(unittest.TestCase):
    def setUp(self):
        dir=os.path.dirname(__file__)
        print(dir)
        chrome_driver_path=dir+"\chromedriver.exe"
        self.browser=webdriver.Chrome(chrome_driver_path)
        self.browser.get("https://www.whatismyip.com/ip-address-lookup/")
        time.sleep(1)

    def tearDown(self):
        self.browser.quit()
    
    def test_GetMyIP(self):
        MyIP=self.browser.find_element_by_name("ip").get_attribute("value")
        return(MyIP)



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
    server = smtplib.SMTP('Smtp.live.com', '25')
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username, password)
    server.sendmail(from_addr, to_addrs, msg.as_string())
    server.quit()


def send_to_addr(username, password, from_addr, to_addrs, msg):

    print('send_to_addr')
    # Read to_addrs email list txt
    #email_list = [line.strip() for line in open('/home/pi/python_code/email.txt')] #for linux
    email_list = [line.strip() for line in open('C:/workspace/selenium/src/pi/email.txt')] #for windows

    for to_addrs in email_list:
        msg = MIMEMultipart()

        msg['Subject'] = "Hello How are you ?" + MyIP
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
            print "Email successfully sent to", to_addrs
        #The sever doesn't accept username and password
        except SMTPAuthenticationError:
            print 'SMTPAuthenticationError'
            print "Email not sent to", to_addrs


if __name__=='__main__':
    unittest.main()

    