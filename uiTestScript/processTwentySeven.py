#coding=utf-8
__author__ = 'xiyuanbupt'
from process import Process
import time
from selenium import webdriver
class ProcessTwentySeven(Process):
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
        Process.__init__(self,driver=driver,projId=projId,tpltId=26,userCount=userCount,userPass=userPass)

    def completeProSix(self,filePath):
        '''
        完成工序27
        filePath为输入文件的路径
        :param theStaffs:
        :return:
        '''
        self.getPage()
        fileIn=self.driver.find_element_by_css_selector("html.ng-scope body div.ng-scope div.wrap.ng-scope div.wrap_r div.w_r_t div.ng-scope div.wrt_xxin.ng-scope div.ng-scope form.ng-scope.ng-pristine.ng-valid div.wrt_xxin_l div.wrt_x_l_c div.wrt_xlc_tab4 div.wrt_ctab4_li label input.tab4_files")
        fileIn.send_keys(filePath)
        tmp=self.driver.find_elements_by_css_selector("html.ng-scope body div.ng-scope div.wrap.ng-scope div.wrap_r div.w_r_t div.ng-scope div.wrt_xxin.ng-scope div.ng-scope form.ng-scope.ng-pristine.ng-valid div.wrt_xxin_l div.wrt_x_l_c div.wrtxlc_sub div.ng-scope input.yh.ng-scope")
        submit=tmp[1]
        submit.click()
        time.sleep(3)
        through=self.driver.find_elements_by_css_selector("html.ng-scope body div.ng-scope div.wrap.ng-scope div.wrap_r div.w_r_t div.ng-scope div.wrt_xxin.ng-scope div.ng-scope form.ng-scope.ng-pristine.ng-valid div.wrt_xxin_l div.wrt_x_l_c div.wrtxlc_sub div.ng-scope input.yh.ng-scope")
        for item in through:
            value=item.get_attribute("value")
            if value==u"通过":
                item.click()
                time.sleep(3)
                break
        recArchive=self.driver.find_element_by_css_selector("html.ng-scope body div.ng-scope div.wrap.ng-scope div.wrap_r div.w_r_t div.ng-scope div.wrt_xxin.ng-scope div.ng-scope form.ng-scope.ng-pristine.ng-valid div.wrt_xxin_l div.wrt_x_l_c div.wrtxlc_sub div.ng-scope input.yh.ng-scope")
        recArchive.click()
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
        processSix=ProcessTwentySeven(driver,5)
        arg='/Users/xiyuanbupt/PycharmProjects/yunZhaoBiao/LoginPage.py'
        if processSix.judgeFinish()==False:
            print u"这个工序未完成"
            processSix.completeProSix(arg)
        else:
            print u'这个工序完成了'

if __name__=="__main__":
    ProcessTwentySeven.unitTest()