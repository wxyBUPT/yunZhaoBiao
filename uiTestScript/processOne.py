#coding=utf-8
__author__ = 'xiyuanbupt'
from LoginPage import LoginPage
from selenium import webdriver
import time
from process import Process

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
        appointTracker=self.driver.find_element_by_css_selector("html.ng-scope body div.ng-scope div.wrap.ng-scope div.wrap_r div.w_r_t div.ng-scope div.wrt_xxin.ng-scope div.ng-scope div.wrt_xxin_l.ng-scope div.wrt_x_l_c div.ng-scope div.wrtxlc_sub input.yh")
        appointTracker.click()
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
        appointRegister=self.driver.find_element_by_css_selector("html.ng-scope body div.ng-scope div.wrap.ng-scope div.wrap_r div.w_r_t div.ng-scope div.wrt_xxin.ng-scope div.ng-scope div.wrt_xxin_l.ng-scope div.wrt_x_l_c div.ng-scope div.wrtxlc_sub input.yh")
        appointRegister.click()
        time.sleep(3)
        recRegist=self.driver.find_element_by_css_selector("html.ng-scope body div.ng-scope div.wrap.ng-scope div.wrap_r div.w_r_t div.ng-scope div.wrt_xxin.ng-scope div.ng-scope div.wrt_xxin_l.ng-scope div.wrt_x_l_c div.wrtxlc_sub.ng-scope input.yh.ng-scope")
        recRegist.click()
        return True

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
        proZero=ProcessOne(driver,21)
        proZero.completeProZero()

if __name__=="__main__":
    print u'执行单元测试'
    ProcessOne.unitTest()
    print u'单元测试执行完毕'