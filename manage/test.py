#coding=utf-8
__author__ = 'xiyuanbupt'

import os
import sys
import imp
import datetime
import conf.conf as testConf
import re
import json
from conf.conf import logger,EmailAdd,SmtpEmailSender

class TestForOneTime(object):
    '''
    执行一次测试，对应功能为执行uiTestScript目录里面的所有
    的测试脚本，如果有Bug则需要给相应的前后端作者以及测试人员发送邮件，
    注意对应一个人一次执行只要发送一封邮件不需要多发送
    '''
    dictEmailInfo={}
    def __init__(self):
        self.testTime=datetime.datetime.now()
        a=[x for x in os.listdir(testConf.uiTestScriptDir) if ((re.search(r'\.py$',x)) and not (re.match(r'__init__\.py',x)) )]
        self.listMoudle=[x.split('.')[0] for x in a]
        sys.path.insert(0,testConf.uiTestScriptDir)
        logger.info(u' ')
        logger.info(u'本次执行测试 %s'%(a))

    def __addEmailInfo(self,res,testScript):
        '''
        根据res结果向dictEmailInfo 中添加信息
        :param res:
        :return:
        '''
        info={}
        info['testFile']=u'%s%s'%(testConf.uiTestScriptDir,testScript)
        info['failPicDir']=res['failPicDir']
        info['detail']=res['detail']
        info['des']=res['des']
        info['backEndDeveloper']=res['backEndDeveloper']
        info['frontEndDeveloper']=res['frontEndDeveloper']
        info['uiTester']=res['uiTester']

        def addInfoTo(developer):
            if res[developer]==None:
                return 0
            if not self.dictEmailInfo.has_key(res[developer]):
                self.dictEmailInfo[res[developer]]=[]
            else:
                pass
            self.dictEmailInfo[res[developer]].append(info)
            return 1

        listToAdd=['backEndDeveloper','frontEndDeveloper','uiTester']
        for developer in listToAdd:
            addInfoTo(developer)

    def runTest(self):
        for i in self.listMoudle:
            logger.info(u'执行%s'%(i))
            a=imp.find_module(i)
            mod_all=imp.load_module(i,a[0],a[1],a[2])
            uiTest=mod_all.uiTest
            uiTest.runTest()
            res=uiTest.getRes()
            res=json.loads(res)
            if res['res']==0:
                self.__addEmailInfo(res,'%s.py'%(i))
                logger.info(u'ui测试%s失败'%(i))
            else:
                logger.info(u'ui测试%s成功'%(i))

    def __getEmaiTab(self,listInfo):
        '''
        返回tablib格式的给这个用户的Bug列表
        :param user:
        :param listInfo:
        :return:
        '''
        import tablib
        headers=(u'模块描述',u'测试文件',u'测试文件返回的错误描述',u'运行图片文件路径',u'后台开发人员',
                 u'前端开发人员',u'测试用例编写人员')
        data=[]
        for info in listInfo:
            aline=[]
            attris=('des','testFile','detail','failPicDir','backEndDeveloper','frontEndDeveloper',
                   'uiTester')
            for attri in attris:
                aline.append(info[attri])
            data.append(aline)
        return tablib.Dataset(*data,headers=headers)

    def sendMail(self):
        for key in self.dictEmailInfo:
            receiverEmail=EmailAdd[key]
            a=self.__getEmaiTab(self.dictEmailInfo[key])
            SmtpEmailSender().sendEmailTo(receiverEmail,a.html)

if __name__=="__main__":
    #a=TestForOneTime()
    #a.runTest()
    #a.sendMail()
    import traceback
    try:
        1/0
    except Exception,e:
        print traceback.format_exc()
        a='%s'%(traceback.format_exc())
        print a