#coding=utf-8
__author__ = 'xiyuanbupt'
#执行测试的逻辑模块
from manage import test
from datetime import datetime,timedelta
from conf.conf import logger
import traceback

def runTest():
    oneTest=test.TestForOneTime()
    oneTest.runTest()
    oneTest.sendMail()
    oneTest.plot()

#下面为每天定时执行的代码，每天八点执行
import time
SECONDS_PER_DAY=24*60*60

def calcReminSeconds(testTime=None):
    '''
    计算当前时间距离需要执行测试时间间隔的秒数
    :return:
    '''
    curTime=datetime.now()
    if curTime.time()<testTime:
        testDateTime=curTime.replace(hour=testTime.hour,minute=testTime.minute,second=testTime.second,microsecond=testTime.microsecond)
        pass
    elif curTime.time()==testTime:
        return 0
    else:
        testDateTime=curTime.replace(day=curTime.day+1,hour=testTime.hour,minute=testTime.minute,second=testTime.second,microsecond=testTime.microsecond)
        pass
    return (testDateTime-curTime).total_seconds()

def run(testTime=None):
    if testTime==None:
        testTime=datetime.time(hour=8)
    while True:
        try:
            sleepSeconds=calcReminSeconds(testTime)
            time.sleep(sleepSeconds)
            runTest()
        except Exception,e:
            logger.warning(u'今天的测试任务出现了bug')
            logger.warning(u'%s'%(traceback.format_exc()))
            from conf.conf import SmtpEmailSender
            sender=SmtpEmailSender()
            sender.sendEmailTo('1223994635@qq.com',traceback.format_exc())
            print traceback.format_exc()

if __name__=="__main__":
    from conf.conf import testTime
    testTime=(datetime.now()+timedelta(seconds=1)).time()
    a=run(testTime)