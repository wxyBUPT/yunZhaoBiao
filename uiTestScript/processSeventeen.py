#coding=utf-8
__author__ = 'xiyuanbupt'
from process import Process
import time
from selenium import webdriver
class ProcessSeventeen(Process):
    '''
    工序十七的自动化测试
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
        Process.__init__(self,driver=driver,projId=projId,tpltId=16,userCount=userCount,userPass=userPass)

    def completeProSix(self,theStaffs):
        '''
        完成工序16
        theStaff为一个列表，列表元素为开标人员的名字
        :param theStaffs:
        :return:
        '''
        self.getPage()
        staffs=self.driver.find_element_by_css_selector("html.ng-scope body div.ng-scope div.wrap.ng-scope div.wrap_r div.w_r_t div.ng-scope div.wrt_xxin.ng-scope div.ng-scope div.wrt_xxin_l.ng-scope div.wrt_x_l_c div.wrt_x_l_tb1_inpt div.wrt_xltb1it_li select.wrtxlc_li_txt1.yh.ng-pristine.ng-valid")
        staffs=staffs.find_elements_by_xpath("option")
        for theStaff in theStaffs:
            for staff in staffs:
                if staff.text==theStaff:
                    staff.click()
        buttons=self.driver.find_elements_by_css_selector("html.ng-scope body div.ng-scope div.wrap.ng-scope div.wrap_r div.w_r_t div.ng-scope div.wrt_xxin.ng-scope div.ng-scope div.wrt_xxin_l.ng-scope div.wrt_x_l_c div.wrtxlc_sub div.ng-scope input.yh")
        print u'找到%d个button'%len(buttons)
        for button in buttons:
            value=button.get_attribute("value")
            print value
            if value==u'通过网络流程':
                time.sleep(1)
                button.click()
                time.sleep(3)
                break
        buttons=self.driver.find_elements_by_css_selector("html.ng-scope body div.ng-scope div.wrap.ng-scope div.wrap_r div.w_r_t div.ng-scope div.wrt_xxin.ng-scope div.ng-scope div.wrt_xxin_l.ng-scope div.wrt_x_l_c div.wrtxlc_sub div.ng-scope input.yh")
        print u'找到%d个button'%len(buttons)
        for button in buttons:
            value=button.get_attribute("value")
            print value
            if value==u'提  交':
                button.click()
                time.sleep(3)
                break
        buttons=self.driver.find_elements_by_css_selector("html.ng-scope body div.ng-scope div.wrap.ng-scope div.wrap_r div.w_r_t div.ng-scope div.wrt_xxin.ng-scope div.ng-scope div.wrt_xxin_l.ng-scope div.wrt_x_l_c div.wrtxlc_sub div.ng-scope input.yh")
        print u'找到%d个button'%len(buttons)
        for button in buttons:
            value=button.get_attribute("value")
            print value
            if value==u'通  过':
                button.click()
                time.sleep(3)
                break
        return True

    @staticmethod
    def unitTest():
        '''
        单元测试
        :return:
        '''
        driver=webdriver.Firefox()
        driver.implicitly_wait(10)
        processSix=ProcessSeventeen(driver,4)
        arg=[u'刘兆君',]
        processSix.completeProSix(arg)

if __name__=="__main__":
    ProcessSeventeen.unitTest()