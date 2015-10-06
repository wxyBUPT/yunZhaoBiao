#coding=utf-8
__author__ = 'xiyuanbupt'
from process import Process
import time
from selenium import webdriver
class ProcessThirty(Process):
    '''
    工序三十的自动化测试
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
        Process.__init__(self,driver=driver,projId=projId,tpltId=29,userCount=userCount,userPass=userPass)

    def completeProThirty(self):
        '''
        完成工序30
        :return:
        '''
        self.getPage()
        finishButton=self.driver.find_element_by_css_selector("html.ng-scope body div.ng-scope div.wrap.ng-scope div.wrap_r div.w_r_t div.ng-scope div.wrt_xxin.ng-scope div.ng-scope div.wrt_xxin_l.ng-scope div.wrt_x_l_ctab1 div.wrtxlc_sub.ng-scope input.yh.ng-scope")
        finishButton.click()
        time.sleep(1)
        confirm=self.driver.find_element_by_css_selector("html.ng-scope body div div.sweet-alert.showSweetAlert.visible button.confirm")
        confirm.click()
        time.sleep(3)
        clean=self.driver.find_element_by_css_selector("html.ng-scope body div.ng-scope div.wrap.ng-scope div.wrap_r div.w_r_t div.ng-scope div.wrt_xxin.ng-scope div.ng-scope div.wrt_xxin_l.ng-scope div.wrt_x_l_ctab1 div.wrtxlc_sub.ng-scope input.yh.ng-scope")
        clean.click()
        time.sleep(1)
        confirm=self.driver.find_element_by_css_selector("html.ng-scope body div div.sweet-alert.showSweetAlert.visible button.confirm")
        confirm.click()
        time.sleep(3)
        end=self.driver.find_element_by_css_selector("html.ng-scope body div.ng-scope div.wrap.ng-scope div.wrap_r div.w_r_t div.ng-scope div.wrt_xxin.ng-scope div.ng-scope div.wrt_xxin_l.ng-scope div.wrt_x_l_ctab1 div.wrtxlc_sub.ng-scope input.yh.ng-scope")
        end.click()
        confirm=self.driver.find_element_by_css_selector("html.ng-scope body div div.sweet-alert.showSweetAlert.visible button.confirm")
        confirm.click()
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
        processThirty=ProcessThirty(driver,5)
        if processThirty.judgeFinish()==False:
            print u"这个工序未完成"
            processThirty.completeProThirty()
        else:
            print u'这个工序完成了'

if __name__=="__main__":
    ProcessThirty.unitTest()