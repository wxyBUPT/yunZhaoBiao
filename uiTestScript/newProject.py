#coding=utf-8
__author__ = 'xiyuanbupt'
import time
from LoginPage import LoginPage
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class NewProject(object):
    '''
    创建新的项目
    '''
    def __init__(self,driver,userCount='zhaobiao@163.com',userPass='test'):
        '''
        初始化
        userCount代表某个用户新建的项目
        :param driver:
        :return:
        '''
        self.driver=driver
        self.loginPage=LoginPage(self.driver)
        self.userCount=userCount
        self.userPass=userPass

    def createNewProject(self,projectInfo,traceback=[],userCount=None,userPass=None):
        '''
        创建新的项目，projectInfo 为必选参数，为项目信息录入的数组，其中
        projectInfo[4]不能为空，并且projectInfo和tarceback必须有长度的保证
        :param projectInfo:
        :param traceback:
        :return:
        '''
        if userCount==None or userPass==None:
            userCount=self.userCount
            userPass=self.userPass
        self.loginPage.login(userCount,userPass)
        newProjectButton=self.driver.find_element_by_css_selector(".wrt_title > label:nth-child(1) > a:nth-child(1)")
        print u'newProjectButton是%s'%newProjectButton
        newProjectButton.click()
        print u'定位新建项目输入'
        proInput=self.driver.find_element_by_css_selector("html.ng-scope body div.ng-scope div.wrap.ng-scope div.wrap_r div.w_r_t div.ng-scope div.wrt_xxin.ng-scope div.ng-scope div.wrt_xxin_l.ng-scope div.wrt_x_l_c div.wrt_x_l_tb1_inpt")
        print u'定位新建项目输入成功'
        #print proInput
        proInputs=proInput.find_elements_by_xpath("div")
        #print proInputs
        for i in range(0,len(proInputs)):
            span=proInputs[i].find_element_by_xpath("span")
            cont=proInputs[i].find_element_by_xpath("input")
            cont.clear()
            cont.send_keys(projectInfo[i])
            cont.send_keys(Keys.TAB)
            print u'%s录入成功'%span.text
        if traceback!=[]:
            tarce=self.driver.find_elements_by_css_selector("html.ng-scope body div.ng-scope div.wrap.ng-scope div.wrap_r div.w_r_t div.ng-scope div.wrt_xxin.ng-scope div.ng-scope div.wrt_xxin_l.ng-scope div.wrt_x_l_c div.wrt_x_l_tb1_inpt")
            tarce=tarce[1]
            traces=tarce.find_elements_by_xpath("div")
            for i in range(0,len(traces)):
                span=traces[i].find_element_by_xpath("span")
                cont=traces[i].find_element_by_xpath("input")
                cont.clear()
                cont.send_keys(traceback[i])
                cont.send_keys(Keys.TAB)
                print u'%s录入成功'%span.text
        else:
            pass
        print u'项目信息以及跟踪反馈结果输入完毕，下面保存输入结果'
        saveButton=self.driver.find_element_by_css_selector("html.ng-scope body div.ng-scope div.wrap.ng-scope div.wrap_r div.w_r_t div.ng-scope div.wrt_xxin.ng-scope div.ng-scope div.wrt_xxin_l.ng-scope div.wrt_x_l_c div.wrtxlc_sub input.yh.ng-scope")
        saveButton.click()
        print u'保存项目成功'

    def getNewProjectId(self):
        '''
        在新建项目后获得新建的项目的projId
        #http://test.zhaobiaosys.com/#/project?projId=12&tpltId=0
        :return:
        '''
        time.sleep(1)
        url=self.driver.current_url
        tmp=url.split('&')
        tmp=tmp[0]
        tmp=tmp.split('=')
        tmp=tmp[1]
        return int(tmp)

    @staticmethod
    def unitTest():
        '''
        单元测试
        可以当做新建项目的测试
        :return:
        '''
        import sys
        reload(sys)
        sys.setdefaultencoding("utf-8")
        import xlrd,csv
        driver=webdriver.Firefox()
        driver.implicitly_wait(10)
        newProject=NewProject(driver)
        f=xlrd.open_workbook('yunZhaoBiaoTest.xlsx')
        newProjectInof=f.sheet_by_name('newProject')
        f=open('newProjectRes.csv','wb')
        writer=csv.writer(f)
        writer.writerow([u'项目信息录入结果',u'备注',u'跟踪反馈结果',u'备注'])
        for row in range(1,newProjectInof.nrows):
            rowValue=newProjectInof.row_values(row)
            proInfo=rowValue[0:9]
            traceInfo=rowValue[9:]
            newProject.createNewProject(proInfo,traceInfo)
            print u'创建项目%d成功'
            writer.writerow([u'success',u'',u'success',u''])

if __name__=="__main__":
    print u'执行新建项目的测试'
    print u'新建项目测试'
    NewProject.unitTest()
    print u'新建项目测试完毕'