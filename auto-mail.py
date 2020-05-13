#!/usr/bin/env python3
from email.mime.text import MIMEText
import os
import smtplib
import ssl
import datetime
import getpass
import re

path = os.getenv("HOME")+"/note/unix/unix.org"
f = open(path, mode="r")
full_text = f.read()

for line in str(full_text).split():
    m = re.search("2\d*-\d*-\d*", line.strip())
    if (m != None):
        break


class Mail():
    def __init__(self):
        self.account = "dld19037@nuc.kwansei.ac.jp"
        self.password = getpass.getpass("enter your password :")
        self.to_addr = "unix-bof@lsnl.jp"
        self.from_addr = "taisei@kwansei.ac.jp"
        self.subject = "(開催通知) UNIXを楽しむ会 " +\
            m.group() + " (水) 12:40/13:30"
        self.context = ssl.create_default_context()

    def message(self):
        self.msg = MIMEText(full_text)
        self.msg["Subject"] = self.subject
        self.msg["To"] = self.to_addr
        self.msg["From"] = self.from_addr
        return str(self.msg).encode("utf-8")

    def main_function(self):
        server = "smtp.office365.com"
        port = "587"
        server = smtplib.SMTP(server, port)
        server.starttls(context=self.context)
        server.login(self.account, self.password)
        server.sendmail(self.from_addr, self.to_addr, self.message())
        server.quit()


def main():
    mail = Mail()
    mail.main_function()


main()
