#coding=utf-8
__author__ = 'xiyuanbupt'
from LoginPage import LoginPage
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

class Message(object):
    '''
    通知界面
    '''
    def __init__(self,driver,userCount='zhaobiao@163.com',userPass='test'):
        '''
        初始化
        :param driver:
        :param userName:
        :param userPass:
        :return:
        '''
        self.driver=driver
        self.userCount=userCount
        self.userPass=userPass
        self.url='http://test.zhaobiaosys.com/#/message'

    def getPage(self):
        '''
        获取对应登录身份的message页面
        :return:
        '''
        loginPage=LoginPage(self.driver)
        loginPage.login(self.userCount,self.userPass)
        self.driver.get('')
        self.driver.get(self.url)

    def newTask(self,addresseeList=[],typeInd=[],processId=[],message=u''):
        '''
        当前用户新建一个任务，
        addresseeList 为任务接受人姓名组成的列表
        :param addresseeList:
        :param typeIndex:
        :param processId:
        :param message:
        :return:
        '''
        newButton=self.driver.find_element_by_css_selector(".add")
        newButton.click()
        append=self.driver.find_element_by_css_selector(".mage_tchnrtr_s")
        append.click()
        messageReceivers=self.driver.find_elements_by_css_selector("label.ng-scope")
        for addressee in addresseeList:
            for receive in messageReceivers:
                if receive.text==addressee:
                    print receive.text
                    print receive
                    print receive.get_attribute('class')
                    print receive.is_displayed()
                    print receive.location
                    receive.click()
                    messageReceivers=self.driver.find_elements_by_css_selector("label.ng-scope")
                    break
        types=self.driver.find_elements_by_css_selector(".ng-dirty > option")
        for type in types:
            print type.text

    @staticmethod
    def unitTest():
        '''
        单元测试
        :return:
        '''
        driver=webdriver.Firefox()
        driver.implicitly_wait(10)
        message=Message(driver)
        message.getPage()
        message.newTask(addresseeList=[u'郭帅',])

if __name__=="__main__":
    Message.unitTest()
