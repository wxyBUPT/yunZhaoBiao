#coding=utf-8
__author__ = 'xiyuanbupt'
import json
from LoginPage import LoginPage
from selenium import webdriver
import time
from process import Process
from testBase import TestBase

class ProcessOne(Process):
    '''
    工序0的自动化测试，根据项目的projId初始化
    '''
    def __init__(self,driver,projId,userCount='zhaobiao@163.com',userPass='test'):
        '''
        根据项目的projId初始化，默认完成工序0的用户是管理员
        :param projId:
        :param userCount:
        :param userPass:
        :return:
        '''
        Process.__init__(self,driver=driver,projId=projId,tpltId=0,userCount=userCount,userPass=userPass)
        #http://test.zhaobiaosys.com/#/project?projId=12&tpltId=0
        self.detail=[]
        self.success=False
        self.success=self.completeProZero()

    def completeProZero(self,TARList=[[u'郭帅',u'刘兆君'],u'季丽娜']):
        '''
        完成工序0
        其中TARList代表 Tarcker And Register List
        即是一个包含参数的列表
        TARList[0]长度不固定，
        TARList[1]长度为1
        :param TARList:
        :return:
        '''
        tracker=TARList[0]
        register=TARList[1]
        self.getPage()
        #http://test.zhaobiaosys.com/#/index?projId=12&tpltId=0
        #http://test.zhaobiaosys.com/#/project?projId=12&tpltId=0
        tmpOptions=self.driver.find_element_by_css_selector('html.ng-scope body div.ng-scope div.wrap.ng-scope div.wrap_r div.w_r_t div.ng-scope div.wrt_xxin.ng-scope div.ng-scope div.wrt_xxin_l.ng-scope div.wrt_x_l_c div.ng-scope div.wrt_xltb1it_li select.wrtxlc_li_txt1.yh.ng-pristine.ng-valid')
        options=tmpOptions.find_elements_by_xpath('option')
        for name in tracker:
            for option in options:
                if name==option.text:
                    option.click()
        self.detail.append(u'选择相应的跟踪人成功，跟踪人包括%s'%(tracker))
        appointTracker=self.driver.find_element_by_css_selector("html.ng-scope body div.ng-scope div.wrap.ng-scope div.wrap_r div.w_r_t div.ng-scope div.wrt_xxin.ng-scope div.ng-scope div.wrt_xxin_l.ng-scope div.wrt_x_l_c div.ng-scope div.wrtxlc_sub input.yh")
        appointTracker.click()
        self.detail.append(u'成功的选择了跟踪人')
        time.sleep(3)
        tmp=self.driver.find_elements_by_css_selector("html.ng-scope body div.ng-scope div.wrap.ng-scope div.wrap_r div.w_r_t div.ng-scope div.wrt_xxin.ng-scope div.ng-scope div.wrt_xxin_l.ng-scope div.wrt_x_l_c div.wrtxlc_sub div.ng-scope input.yh.ng-scope")
        feedbackTrackingInfo=tmp[0]
        print u'点击了%s'%feedbackTrackingInfo.text
        print u'rect:%s'%feedbackTrackingInfo.rect
        print u'parent:%s'%feedbackTrackingInfo.parent
        print u'tagName:%s'%feedbackTrackingInfo.tag_name
        print u'value %s'%feedbackTrackingInfo.get_attribute('value')
        feedbackTrackingInfo.click()
        time.sleep(3)
        proRegisters=self.driver.find_element_by_css_selector("html.ng-scope body div.ng-scope div.wrap.ng-scope div.wrap_r div.w_r_t div.ng-scope div.wrt_xxin.ng-scope div.ng-scope div.wrt_xxin_l.ng-scope div.wrt_x_l_c div.ng-scope div.wrt_x_l_tb1_inpt div.wrt_xltb1it_li select.wrtxlc_li_txt1.yh.ng-pristine.ng-valid")
        options=proRegisters.find_elements_by_xpath('option')
        for option in options:
            if option.text==register:
                option.click()
                time.sleep(3)
                break
        self.detail.append(u'登记人为%s'%(register))
        appointRegister=self.driver.find_element_by_css_selector("html.ng-scope body div.ng-scope div.wrap.ng-scope div.wrap_r div.w_r_t div.ng-scope div.wrt_xxin.ng-scope div.ng-scope div.wrt_xxin_l.ng-scope div.wrt_x_l_c div.ng-scope div.wrtxlc_sub input.yh")
        appointRegister.click()
        time.sleep(3)
        self.detail.append(u'已经选择了登记人')
        recRegist=self.driver.find_element_by_css_selector("html.ng-scope body div.ng-scope div.wrap.ng-scope div.wrap_r div.w_r_t div.ng-scope div.wrt_xxin.ng-scope div.ng-scope div.wrt_xxin_l.ng-scope div.wrt_x_l_c div.wrtxlc_sub.ng-scope input.yh.ng-scope")
        recRegist.click()
        self.detail.append(u'工序0执行完毕')
        return True

    def getDetial(self):
        return self.detail

    @staticmethod
    def unitTest():
        '''
        单元测试
        :return:
        '''
        import sys
        reload(sys)
        sys.setdefaultencoding('utf-8')
        driver=webdriver.Firefox()
        driver.implicitly_wait(5)
        proZero=ProcessOne(driver,61)
        proZero.completeProZero()

class proOneScript(TestBase):
    def _runTest(self,driver,proId):
        '''
        对应的执行逻辑
                print u'我正在执行，相关测试结果需要在这里赋值'
        res={}
        #1 代表执行成功，0代表执行不成功
        res['res']=0
        res['backEndDeveloper']=self.backEndDeveloper
        res['backEndLang']=self.backEndLang
        res['frontEndDeveloper']=self.frontEndDeveloper
        res['frontEndLang']=self.frontEndLang
        res['uiTester']=self.uiTester
        res['traceBack']=None
        res['failPicDir']=None
        #执行过程中需要返回的错误信息
        res['detail']=None
        #初始化的描述信息
        res['des']=self.des
        self.res=res
        '''
        print u'正在执行工序0的测试'
        processOne=ProcessOne(driver,proId)
        res={}
        if processOne.success==True:
            res['res']=1
        else:
            res['res']=0
        res['backEndDeveloper']=self.backEndDeveloper
        res['backEndLang']=self.backEndLang
        res['frontEndDeveloper']=self.frontEndDeveloper
        res['frontEndLang']=self.frontEndLang
        res['uiTester']=self.uiTester
        res['traceBack']=None
        res['failPicDir']=None
        res['detail']=processOne.getDetial()
        res['des']=self.des
        self.res=res

    def getRes(self):
        '''
        规定所有测试类的getRes的返回值必须包含以下参数
        即子类中不管使用什么方法，都要返回正确的res格式
        :return:
        '''
        #print u'getRes在执行'
        import sys
        reload(sys)
        sys.setdefaultencoding('utf-8')
        driver=webdriver.Firefox()
        driver.implicitly_wait(5)
        try:
            self._runTest(driver,57)
        except:
            self.res['res']=0
            print self.res
        driver.close()

        return json.dumps(self.res)

uiTest=proOneScript(description=u'工序0的测试')
#if __name__=="__main__":
#    print u'执行单元测试'
#    ProcessOne.unitTest()
#    print u'单元测试执行完毕'