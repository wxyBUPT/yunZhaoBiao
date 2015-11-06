#coding=utf-8

__author__ = 'xiyuanbupt'
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class LoginPage(object):
    '''
    登录界面
    '''
    def __init__(self,driver,loginUrl='http://test.zhaobiaosys.com/#/login'):
        '''
        初始换参数为一个driver对象
        :param driver:
        :param loginUrl:
        :return:
        '''
        self.loginUrl=loginUrl
        self.driver=driver

    def login(self,loginName='zhaobiao@163.com',loginPass='test'):
        '''
        登录，默认以刘兆君身份登录
        :param loginName:
        :param loginPass:
        :return:
        '''
        print u'获取初始的登录页面'
        self.driver.get('')
        self.driver.get(self.loginUrl)
        print u'获取初始登录界面成功，开始查找元素'
        userName=self.driver.find_element_by_css_selector("form.ng-pristine > p:nth-child(1) > input:nth-child(1)")
        passWord=self.driver.find_element_by_css_selector("p.p2:nth-child(3) > input:nth-child(1)")
        loginButton=self.driver.find_element_by_css_selector("html.ng-scope body div.ng-scope div.login_wrap.ng-scope div.loginfr form.ng-pristine.ng-invalid.ng-invalid-required p.p4 input.yh")
        #print u'获取元素的类型是:%s,获取元素是:%s'%(type(userNameFram),userNameFram)
        userName.clear()
        userName.send_keys(loginName)
        userName.send_keys(Keys.TAB)
        passWord.clear()
        passWord.send_keys(loginPass)
        passWord.send_keys(Keys.TAB)
        loginButton.click()

    def getCurUrl(self):
        '''
        获得页面当前的网址
        :return:
        '''
        time.sleep(1)
        return self.driver.current_url

    def verifiLogin(self):
        '''
        验证是否登录成功，如果登录成功返回登录用户名
        如果登录不成功返回空的unicode字符串
        :return:
        '''
        time.sleep(2)
        res=u''
        try:
            user=self.driver.find_element_by_css_selector("html.ng-scope body div.ng-scope div.wrap.ng-scope div.wrap_l.ng-scope div.w_l_name.ng-scope span.ng-binding")
            print user.text
        except:
            return res
        res=user.text
        return res

    def recoverLoginPage(self):
        '''
        恢复登录界面
        :return:
        '''
        self.driver.get(self.loginUrl)

    @staticmethod
    def unitTest():
        '''
        单元测试
        可以认为是登录页面的验证
        :return:
        '''
        import sys
        reload(sys)
        sys.setdefaultencoding("utf-8")
        import xlrd,csv
        driver=webdriver.Firefox()
        driver.implicitly_wait(10)
        loginPage=LoginPage(driver)
        f=xlrd.open_workbook('yunZhaoBiaoTest.xlsx')
        userCountTable=f.sheet_by_name('userCount')
        f=open('loginRes.csv','wb')
        writer=csv.writer(f)
        writer.writerow([u'登录结果',u'登录人'])
        for row in range(1,userCountTable.nrows):
            info=userCountTable.row_values(row)
            print u'登录账户:%s, 登录密码:%s'%(info[0],info[1])
            #print u'登录当前账户'
            loginPage.login(info[0],info[1])
            res=loginPage.verifiLogin()
            if res==u'':
                writer.writerow([u'loginFail',info[0]])
                print u'%s登录失败'%info[0]
                print u'当前的cookies为'
                print driver.get_cookies()
            else:
                writer.writerow([u'success',res])
                print u'%s登录成功'%info[1]
                print u'当前的cookies为'
                print driver.get_cookies()
        f.close()

if __name__=="__main__":
    LoginPage.unitTest()
    print u'登录测试执行完毕'