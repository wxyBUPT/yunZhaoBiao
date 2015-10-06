#coding=utf-8
__author__ = 'xiyuanbupt'

from LoginPage import LoginPage
class Process(object):
    '''
    所有工序的基类，只包含工序的初始化
    '''
    def __init__(self,driver,projId,tpltId,userCount='zhaobiao@163.com',userPass='test'):
        '''
        根据proId初始化
        '''
        self.driver=driver
        self.url=u'http://test.zhaobiaosys.com/#/project?projId=%d&tpltId=%d'%(projId,tpltId)
        self.userCount=userCount
        self.userPass=userPass
        self.tpltId=tpltId

    def getPage(self):
        '''
        获得对应登录身份的process页面
        :return:
        '''
        loginPage=LoginPage(self.driver)
        loginPage.login(self.userCount,self.userPass)
        self.driver.get('')
        self.driver.get(self.url)

    def judgeFinish(self):
        '''
        判断当前的的工序是否完全完成
        :return:
        '''
        self.getPage()
        finishFlag=(u'li3',u'li3_2')
        processLis=self.driver.find_elements_by_css_selector("html.ng-scope body div.ng-scope div.wrap.ng-scope div.wrap_r div.w_r_t div.ng-scope div.ng-scope div.wrt_gx_c.ng-scope ul li")
        for processLi in processLis:
            if processLi.get_attribute('class') in finishFlag:
                text=processLi.find_element_by_xpath("span").text
                tpltId=self.tpltId+1
                text=text.split('.')
                id=int(text[0])
                if id==tpltId:
                    return True
        return False
