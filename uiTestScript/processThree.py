#coding=utf-8
__author__ = 'xiyuanbupt'
from process import Process
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class ProcessThree(Process):
    '''
    工序三的自动化测试
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
        Process.__init__(self,driver=driver,projId=projId,tpltId=2,userCount=userCount,userPass=userPass)

    def completeProThree(self,args,supArg):
        '''
        完成工序27
        filePath为输入文件的路径
        :param theStaffs:
        :return:
        '''
        self.getPage()
        inputs=self.driver.find_elements_by_css_selector("html.ng-scope body.laydate_body div.ng-scope div.wrap.ng-scope div.wrap_r div.w_r_t div.ng-scope div.wrt_xxin.ng-scope div.ng-scope div.wrt_xxin_l.ng-scope div.wrt_x_l_c form.ng-valid.ng-dirty div.wrt_x_l_tb1_inpt div.wrt_xltb1it_li")
        print type(inputs)
        tmpinputs=[]
        for input in inputs:
            cla=input.get_attribute('class')
            if cla!=u'wrt_ctab4_file':
                tmpinputs.append(input)
            else:
                pass
        inputs=tmpinputs

        for i in range(0,len(args)):
            text=inputs[i].find_element_by_xpath('span').text

            inputs[i].clear()
            inputs[i].send_keys(args[i])
            inputs.send_keys(Keys.TAB)
        return True


    @staticmethod
    def unitTest():
        '''
        单元测试
        :return:
        '''
        driver=webdriver.Firefox()
        driver.implicitly_wait(10)
        processThree=ProcessThree(driver,5)
        if processThree.judgeFinish()==False:
            print u"这个工序未完成"
            processThree.completeProThree()
        else:
            print u'这个工序完成了'

if __name__=="__main__":
    ProcessThree.unitTest()