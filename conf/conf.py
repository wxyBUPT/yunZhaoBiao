#coding=utf-8
__author__ = 'xiyuanbupt'
import datetime

#对应开发人员和相应的邮箱地址，
EmailAdd={
    'wangxiyuan':'1223994635@qq.com',
    'zhongtianlong':'1223994635@qq.com',
}

#定义每天执行测试的时间，目前规定一天执行一次自动化测试，每天早晨八点执行自动化测试
import datetime
testTime=datetime.time(hour=8)

#所有测试脚本的路径，路径中的 .py 脚本都会被执行，为了完成测试任务，每个脚本文件中必须包含特定的参数
uiTestScriptDir='/Users/xiyuanbupt/PycharmProjects/yunZhaoBiao/dirTest/'

#日志文件，当前设置为每个日志最大为10M 最多可以有5个备份，如果运行到后期不能执行，可能因为日志文件满
uiTestLogFile='/Users/xiyuanbupt/PycharmProjects/yunZhaoBiao/runLog/testApp.log'


import smtplib
import logging
from logging.handlers import RotatingFileHandler
from email.mime.text import MIMEText
from email.header import Header

#日志配置
def getLogger(file):
    '''
    获得日志的句柄，
    日志的配置在这里实现
    :return:
    '''
    Rthandler=RotatingFileHandler(file,maxBytes=10*1024*1024,backupCount=5)
    Rthandler.setLevel(logging.DEBUG)
    formatter=logging.Formatter('%(asctime)s-%(filename)s:%(lineno)s-%(name)s-%(message)s')
    Rthandler.setFormatter(formatter)
    logger=logging.getLogger('testLog')
    logger.addHandler(Rthandler)
    logger.setLevel(logging.INFO)
    return logger

#程序中所有的日志都写在这个logger中
logger=getLogger(uiTestLogFile)

#定义了一个简单的Smtp协议发送邮件，目前不支持附件以及图片的发送
class SmtpEmailSender(object):
    def __init__(self):
        self.subject=u'来自自动化测试的bug'
        self.sender='746451950@qq.com'
        self.smtpServer='smtp.qq.com'
        self.username='746451950@qq.com'
        self.password='wxy1992'

    def sendEmailTo(self,receiverEmail,htmlContent):
        msg=MIMEText(u'<html><h1>下面和你相关的Bug</h1><h2>测试执行时间%s</h2><body>%s</body></html>'%(datetime.datetime.now(),htmlContent),'html','utf-8')
        msg['Subject']=Header(self.subject,'utf-8')

        smtp=smtplib.SMTP()
        smtp.connect(self.smtpServer)
        smtp.login(self.username,self.password)
        smtp.sendmail(self.sender,receiverEmail,msg.as_string())
        smtp.quit()