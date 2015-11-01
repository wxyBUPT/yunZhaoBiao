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
        def delRunScript(listMoudle,delList):
            #返回差集
            return [i for i in listMoudle if i not in delList]
        self.listMoudle=delRunScript(self.listMoudle,['LoginPage','process','processOne'])
        print u'需要执行的测试有%s'%(self.listMoudle)
        sys.path.insert(0,testConf.uiTestScriptDir)
        logger.info(u' ')
        logger.info(u'本次执行测试 %s'%(a))
        #下面包含了一些全局的信息，包括总共需要执行了多少脚本，实际执行了多少脚本成功执行的脚本的个数，失败执行的脚本个数
        self.needRunCount=len(self.listMoudle)
        self.runCount=0
        self.failCount=0
        self.sucessCount=0

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
            print mod_all
            uiTest=mod_all.uiTest
            print uiTest
            #uiTest.runTest()
            self.runCount+=1
            tmp=uiTest.getRes()
            print tmp
            tmp=json.loads(tmp)
            if tmp['res']==0:
                self.failCount+=1
                self.__addEmailInfo(tmp,'%s.py'%(i))
                logger.info(u'ui测试%s失败'%(i))
            else:
                self.sucessCount+=1
                logger.info(u'ui测试%s成功'%(i))

    def __getEmaiTab(self,listInfo):
        '''
        返回tablib格式的给这个用户的Bug列表
        :param user:
        :param listInfo:
        :return:
        '''
        import tablib
        headers=[u'模块描述',u'测试文件',u'测试文件返回的错误描述',u'运行图片文件路径',u'后台开发人员',
                 u'前端开发人员',u'测试用例编写人员']
        data=[]
        label=[u'本次需要执行的测试脚本个数',u'本次实际执行的测试脚本个数',u'本次执行成功的脚本个数',u'本次执行失败的脚本个数']
        data.append(label)
        res=[self.needRunCount,self.runCount,self.sucessCount,self.failCount]
        data.append(res)
        for info in listInfo:
            aline=[]
            attris=('des','testFile','detail','failPicDir','backEndDeveloper','frontEndDeveloper',
                   'uiTester')
            for attri in attris:
                aline.append(info[attri])
            data.append(aline)
        #print data
        def verifyData(data,headers):
            '''
            返回维数符合标准的data数据
            :param data:
            :return:
            '''
            maxCount=0
            for line in data:
                l=len(line)
                maxCount=l if l>maxCount else maxCount
            for line in data:
                for i in range(len(line),maxCount):
                    line.append(u'')
            for i in range(len(headers),maxCount):
                headers.append(u'')
        verifyData(data,headers)
        return tablib.Dataset(*data,headers=headers)

    def sendMail(self):
        for key in self.dictEmailInfo:
            receiverEmail=EmailAdd[key]
            a=self.__getEmaiTab(self.dictEmailInfo[key])
            SmtpEmailSender().sendEmailTo(receiverEmail,a.html)

    def plot(self):
        '''
        画图模块，暂时只是做一个演示
        :return:
        '''
        import matplotlib
        import matplotlib.pylab
        y_values=[self.needRunCount,self.runCount,self.failCount,self.sucessCount]
        x_values=[i for i in range(1,len(y_values)+1)]
        fig=matplotlib.pylab.figure()
        ax=fig.add_subplot(111)
        ax.scatter(x_values,y_values)
        matplotlib.pylab.show()

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