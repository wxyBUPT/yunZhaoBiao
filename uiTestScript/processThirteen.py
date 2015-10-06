#coding=utf-8
__author__ = 'xiyuanbupt'
from process import Process
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
class ProcessThirteen(Process):
    '''
    工序十三的自动化测试
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
        Process.__init__(self,driver=driver,projId=projId,tpltId=12,userCount=userCount,userPass=userPass)

    def comIn(self,startTime,endTime):
        '''
        在公司内部开标
        :param startTime:
        :param endTime:
        :return:
        '''
        self.getPage()
        inStartTime=self.driver.find_element_by_css_selector("#expectedOpenTime")
        inStartTime.clear()
        inStartTime.send_keys(startTime)
        inStartTime.send_keys(Keys.TAB)
        submit=self.driver.find_element_by_css_selector(".wrtxlc_sub > div:nth-child(1) > input:nth-child(1)")
        submit.click()
        time.sleep(3)
        start=self.driver.find_elements_by_css_selector("html.ng-scope body.laydate_body div.ng-scope div.wrap.ng-scope div.wrap_r div.w_r_t div.ng-scope div.wrt_xxin.ng-scope div.ng-scope div.wrt_xxin_l.ng-scope div.wrt_x_l_c div.wrtxlc_sub div.ng-scope input.yh.ng-scope")[0]
        start.click()
        time.sleep(3)
        inEndTime=self.driver.find_element_by_css_selector("html.ng-scope body.laydate_body div.ng-scope div.wrap.ng-scope div.wrap_r div.w_r_t div.ng-scope div.wrt_xxin.ng-scope div.ng-scope div.wrt_xxin_l.ng-scope div.wrt_x_l_c div.wrt_x_l_tb1_inpt div.wrt_xltb1it_li.ng-scope input#realOpenTime.laydate-icon.ng-isolate-scope.ng-valid.ng-dirty")
        inEndTime.clear()
        inEndTime.send_keys(endTime)
        inEndTime.send_keys(Keys.TAB)
        submit=self.driver.find_elements_by_css_selector("html.ng-scope body.laydate_body div.ng-scope div.wrap.ng-scope div.wrap_r div.w_r_t div.ng-scope div.wrt_xxin.ng-scope div.ng-scope div.wrt_xxin_l.ng-scope div.wrt_x_l_c div.wrtxlc_sub div.ng-scope input.yh.ng-scope")[0]
        submit.click()
        time.sleep(3)
        pass

    def comOut(self,startTime,endTime):
        '''
        在公司外部开标
        :param startTime:
        :param endTime:
        :return:
        '''
        self.getPage()
        inStartTime=self.driver.find_element_by_css_selector("#expectedOpenTime")
        inStartTime.clear()
        inStartTime.send_keys(startTime)
        inStartTime.send_keys(Keys.TAB)
        submit=self.driver.find_elements_by_css_selector("html.ng-scope body.laydate_body div.ng-scope div.wrap.ng-scope div.wrap_r div.w_r_t div.ng-scope div.wrt_xxin.ng-scope div.ng-scope div.wrt_xxin_l.ng-scope div.wrt_x_l_c div.wrtxlc_sub div.ng-scope input.yh.ng-scope")[0]
        submit.click()
        time.sleep(3)
        start=self.driver.find_elements_by_css_selector("html.ng-scope body.laydate_body div.ng-scope div.wrap.ng-scope div.wrap_r div.w_r_t div.ng-scope div.wrt_xxin.ng-scope div.ng-scope div.wrt_xxin_l.ng-scope div.wrt_x_l_c div.wrtxlc_sub div.ng-scope input.yh.ng-scope")[1]
        start.click()
        time.sleep(3)
        seal=self.driver.find_elements_by_css_selector("html.ng-scope body.laydate_body div.ng-scope div.wrap.ng-scope div.wrap_r div.w_r_t div.ng-scope div.wrt_xxin.ng-scope div.ng-scope div.wrt_xxin_l.ng-scope div.wrt_x_l_c div.wrtxlc_sub div.ng-scope input.yh.ng-scope")[0]
        seal.click()
        time.sleep(3)
        firstSeal=self.driver.find_elements_by_css_selector("html.ng-scope body.laydate_body div.ng-scope div.wrap.ng-scope div.wrap_r div.w_r_t div.ng-scope div.wrt_xxin.ng-scope div.ng-scope div.wrt_xxin_l.ng-scope div.wrt_x_l_c div.wrtxlc_sub div.ng-scope input.yh.ng-scope")[0]
        firstSeal.click()
        time.sleep(3)
        superVisionSeal=self.driver.find_element_by_css_selector("html.ng-scope body.laydate_body div.ng-scope div.wrap.ng-scope div.wrap_r div.w_r_t div.ng-scope div.wrt_xxin.ng-scope div.ng-scope div.wrt_xxin_l.ng-scope div.wrt_x_l_c div.wrtxlc_sub div.ng-scope input.yh.ng-scope")[0]
        superVisionSeal.click()
        time.sleep(3)
        inEndTime=self.driver.find_element_by_css_selector("html.ng-scope body.laydate_body div.ng-scope div.wrap.ng-scope div.wrap_r div.w_r_t div.ng-scope div.wrt_xxin.ng-scope div.ng-scope div.wrt_xxin_l.ng-scope div.wrt_x_l_c div.wrt_x_l_tb1_inpt div.wrt_xltb1it_li.ng-scope input#realOpenTime.laydate-icon.ng-isolate-scope.ng-valid.ng-dirty")
        inEndTime.clear()
        inEndTime.send_keys(endTime)
        inEndTime.send_keys(Keys.TAB)
        appointment=self.driver.find_elements_by_css_selector("html.ng-scope body.laydate_body div.ng-scope div.wrap.ng-scope div.wrap_r div.w_r_t div.ng-scope div.wrt_xxin.ng-scope div.ng-scope div.wrt_xxin_l.ng-scope div.wrt_x_l_c div.wrtxlc_sub div.ng-scope input.yh.ng-scope")[0]
        appointment.click()
        time.sleep(3)
        pass

    def completeThirteen(self,startTime,endTime,inOrOut='in'):
        '''
        完成工序十三
        inOrOut为字符串
        :param startTime:
        :param endTime:
        :param inOrOut:
        :return:
        '''
        if inOrOut=='in':
            self.comIn(startTime,endTime)
        elif inOrOut=='out':
            self.comOut(startTime,endTime)
        else:
            print u'参数非法'
        return True


    @staticmethod
    def unitTest():
        '''
        单元测试
        :return:
        '''
        driver=webdriver.Firefox()
        driver.implicitly_wait(10)
        proThirteen=ProcessThirteen(driver,5)
        if proThirteen.judgeFinish()==False:
            print u"这个工序未完成"
            proThirteen.completeThirteen('2015-09-11 12:12','2014-08-08 12:12')
        else:
            print u'这个工序完成了'

if __name__=="__main__":
    print u'日期框不能定位的问题还未解决'
    ProcessThirteen.unitTest()