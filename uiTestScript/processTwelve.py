#coding=utf-8
__author__ = 'xiyuanbupt'
from process import Process
import time
from selenium import webdriver
class ProcessTwelve(Process):
    '''
    工序十二的自动化测试
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
        Process.__init__(self,driver=driver,projId=projId,tpltId=11,userCount=userCount,userPass=userPass)

    def completeProSix(self):
        '''
        完成工序12
        :return:
        '''
        self.getPage()
        applicatInquiry=self.driver.find_element_by_css_selector("html.ng-scope body div.ng-scope div.wrap.ng-scope div.wrap_r div.w_r_t div.ng-scope div.wrt_xxin.ng-scope div.ng-scope div.wrt_xxin_l.ng-scope div.wrt_x_l_c div.wrtxlc_sub.ng-scope input.yh.ng-scope")
        applicatInquiry.click()
        time.sleep(3)
        agree=self.driver.find_elements_by_css_selector("html.ng-scope body div.ng-scope div.wrap.ng-scope div.wrap_r div.w_r_t div.ng-scope div.wrt_xxin.ng-scope div.ng-scope div.wrt_xxin_l.ng-scope div.wrt_x_l_c div.wrtxlc_sub.ng-scope input.yh.ng-scope")
        agree=agree[0]
        agree.click()
        time.sleep(3)
        seal=self.driver.find_elements_by_css_selector("html.ng-scope body div.ng-scope div.wrap.ng-scope div.wrap_r div.w_r_t div.ng-scope div.wrt_xxin.ng-scope div.ng-scope div.wrt_xxin_l.ng-scope div.wrt_x_l_c div.wrtxlc_sub.ng-scope input.yh.ng-scope")
        seal=seal[0]
        seal.click()
        time.sleep(3)
        executiveInquiry=self.driver.find_elements_by_css_selector("html.ng-scope body div.ng-scope div.wrap.ng-scope div.wrap_r div.w_r_t div.ng-scope div.wrt_xxin.ng-scope div.ng-scope div.wrt_xxin_l.ng-scope div.wrt_x_l_c div.wrtxlc_sub.ng-scope input.yh.ng-scope")
        executiveInquiry=executiveInquiry[0]
        executiveInquiry.click()
        time.sleep(3)
        return True



    @staticmethod
    def unitTest():
        '''
        单元测试
        :return:
        '''
        driver=webdriver.Firefox()
        driver.implicitly_wait(10)
        processSix=ProcessTwelve(driver,18)
        processSix.completeProSix()

if __name__=="__main__":
    ProcessTwelve.unitTest()