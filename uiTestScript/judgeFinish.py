#coding=utf-8
__author__ = 'xiyuanbupt'
from process import Process
from selenium import webdriver
class JudgeFinish(Process):
    '''
    工序二十七的自动化测试
    '''
    def __init__(self,driver,projId,userCount='zhaobiao@163.com',userPass='test'):
        '''
        根据projId初始化
        :param driver:
        :param projId:
        :param userCount:
        :param userPass:
        :return:
        '''
        Process.__init__(self,driver=driver,projId=projId,tpltId=0,userCount=userCount,userPass=userPass)

    def judgeFinish(self):
        '''
        判断这个proj 完成的工序以及未完成的工序
        :param processIdList:
        :return:
        '''
        self.getPage()
        finishFlag=(u'li3',u'li3_2')
        inProgressFlag=(u'li2_2',u'li2')
        noStartFlag=(u'li4',u'li4_2')
        finishList=[]
        overTimeList=[]
        inProgressList=[]
        noStartList=[]
        processLis=self.driver.find_elements_by_css_selector("html.ng-scope body div.ng-scope div.wrap.ng-scope div.wrap_r div.w_r_t div.ng-scope div.ng-scope div.wrt_gx_c.ng-scope ul li")
        for processLi in processLis:
            flag=processLi.get_attribute('class')
            text=processLi.find_element_by_xpath("span").text
            if flag in finishFlag:
                finishList.append(text)
            elif flag in inProgressFlag:
                inProgressList.append(text)
            elif flag in noStartFlag:
                noStartList.append(text)
            else:
                overTimeList.append(text)
        return [finishList,inProgressList,noStartList,overTimeList]

    def getUserRelevant(self):
        '''
        获得与当前用户相关的工序
        :return:
        '''
        self.getPage()
        relFlag=(u'bg_1',)
        relList=[]
        processLis=self.driver.find_elements_by_css_selector("html.ng-scope body div.ng-scope div.wrap.ng-scope div.wrap_r div.w_r_t div.ng-scope div.ng-scope div.wrt_gx_c.ng-scope ul li")
        for processLi in processLis:
            try:
                flag=processLi.find_element_by_xpath('b').get_attribute('class')
                if flag in relFlag:
                    text=processLi.find_element_by_xpath('span').text
                    relList.append(text)
            except:
                pass
        return relList
        pass

    @staticmethod
    def unitTest():
        '''
        单元测试
        :return:
        '''
        driver=webdriver.Firefox()
        driver.implicitly_wait(10)
        judgeFiish=JudgeFinish(driver,18,'guoshuai@163.com','test')
        condition=judgeFiish.judgeFinish()
        print u'执行完成的工序有'
        for item in condition[0]:
            print item
        print u'正在执行的任务有'
        for item in condition[1]:
            print item
        print u'未开始的任务有'
        for item in condition[2]:
            print item
        print u'即将超期或者超期的任务有'
        for item in condition[3]:
            print item
        condition=judgeFiish.getUserRelevant()
        print u'与当前用户相关的工序有'
        for item in condition:
            print item

if __name__=="__main__":
    JudgeFinish.unitTest()