#coding=utf-8
__author__ = 'xiyuanbupt'
from process import Process
import time
from selenium import webdriver
class ProcessSix(Process):
    '''
    工序六的自动化测试
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
        Process.__init__(self,driver=driver,projId=projId,tpltId=5,userCount=userCount,userPass=userPass)

    def completeProSix(self):
        '''
        完成工序6
        :return:
        '''
        self.getPage()
        print u'查找元素'
        print self.driver
        time.sleep(1)
        submit=self.driver.find_element_by_css_selector("html.ng-scope body div.ng-scope div.wrap.ng-scope div.wrap_r div.w_r_t div.ng-scope div.wrt_xxin.ng-scope div.ng-scope div.wrt_xxin_l.ng-scope div.wrt_x_l_c div.wrtxlc_sub.ng-scope input.yh.ng-scope")
        print u'找到元素'
        submit.click()
        time.sleep(3)
        tmp=self.driver.find_elements_by_css_selector("html.ng-scope body div.ng-scope div.wrap.ng-scope div.wrap_r div.w_r_t div.ng-scope div.wrt_xxin.ng-scope div.ng-scope div.wrt_xxin_l.ng-scope div.wrt_x_l_c div.wrtxlc_sub.ng-scope input.yh.ng-scope")
        examine=tmp[0]
        examine.click()
        time.sleep(3)
        tmp=self.driver.find_elements_by_css_selector("html.ng-scope body div.ng-scope div.wrap.ng-scope div.wrap_r div.w_r_t div.ng-scope div.wrt_xxin.ng-scope div.ng-scope div.wrt_xxin_l.ng-scope div.wrt_x_l_c div.wrtxlc_sub.ng-scope input.yh.ng-scope")
        seal=tmp[0]
        seal.click()
        time.sleep(3)
        tmp=self.driver.find_elements_by_css_selector("html.ng-scope body div.ng-scope div.wrap.ng-scope div.wrap_r div.w_r_t div.ng-scope div.wrt_xxin.ng-scope div.ng-scope div.wrt_xxin_l.ng-scope div.wrt_x_l_c div.wrtxlc_sub.ng-scope input.yh.ng-scope")
        finish=tmp[0]
        finish.click()
        time.sleep(2)
        return True

    @staticmethod
    def unitTest():
        '''
        单元测试
        :return:
        '''
        driver=webdriver.Firefox()
        driver.implicitly_wait(10)
        processSix=ProcessSix(driver=driver,projId=19)
        processSix.completeProSix()

if __name__=="__main__":
    ProcessSix.unitTest()