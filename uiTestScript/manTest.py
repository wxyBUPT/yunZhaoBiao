#coding=utf-8
__author__ = 'xiyuanbupt'
from newProject import NewProject
from selenium import webdriver
import unittest

class ManTest(unittest.TestCase):

    def setUp(self):
        driver=webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.get('')
        projInfo=[u'',u'',u'',u'',u'Selenium自动化测试',u'',u'',u'',u'']
        newPro=NewProject(driver)
        newPro.createNewProject(projInfo)
        self.proId=newPro.getNewProjectId()
        self.driver=driver

    def tearDown(self):
        pass

    def testProcessOne(self):
        from processOne import ProcessOne
        proOne=ProcessOne(self.driver,self.proId)
        self.assertTrue(proOne.completeProZero())

    def testProcessThree(self):
        from processThree import ProcessThree
        proThree=ProcessThree(self.driver,self.proId)
        self.assertTrue(proThree.completeProThree())

    def testProcessFive(self):
        from processFive import ProcessFive
        proFive=ProcessFive(self.driver,self.proId)
        self.assertTrue(proFive.completeProSix())

    def testProcessSix(self):
        from processSix import ProcessSix
        proSix=ProcessSix(self.driver,self.proId)
        self.assertTrue(proSix.completeProSix())

    def testProcessThirty(self):
        from peocessThirty import ProcessThirty
        proThirty=ProcessThirty(self.driver,self.proId)
        self.assertTrue(proThirty.completeProThirty())

    def testProcessSeventeen(self):
        from processSeventeen import ProcessSeventeen
        proSeventeen=ProcessSeventeen(self.driver,self.proId)
        arg=[u'刘兆君',]
        self.assertTrue(proSeventeen.completeProSix(arg))

    def testProcessThirteen(self):
        from processThirteen import ProcessThirteen
        proThirteen=ProcessThirteen(self.driver,self.proId)
        self.assertTrue(proThirteen.completeThirteen('2015-09-11 12:12','2014-08-08 12:12'))

    def testProcessTwelve(self):
        from processTwelve import ProcessTwelve
        proTwelve=ProcessTwelve(self.driver,self.proId)
        self.assertTrue(proTwelve.completeProSix())

    def testProcessTwentySeven(self):
        from processTwentySeven import ProcessTwentySeven
        proTwentySeven=ProcessTwentySeven(self.driver,self.proId)
        arg='/Users/xiyuanbupt/PycharmProjects/yunZhaoBiao/LoginPage.py'
        self.assertTrue(proTwentySeven.completeProSix(arg))

if __name__=="__main__":
    unittest.main()