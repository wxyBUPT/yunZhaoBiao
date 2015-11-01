#coding=utf-8
__author__ = 'xiyuanbupt'
import json

class TestBase(object):
    '''
    规定所有测试类都应该实现的接口
    '''
    def __init__(self,backEndDeveloper=None,backEndLang=None,frontEndDeveloper=None,
                 frontEndLan=None,uiTester='wangxiyuan',
                 description=u'本次是基类的测试'):
        '''
        初始化信息都是为了如果出错发送邮件通知相关人员
        :param backEndDeveloper: 后台开发人员
        :param backEndLang: 后台开发语言
        :param frontEndDeveloper: 前端开发人员
        :param frontEndLan: 前端语言
        :param uiTester: 执行测试人员
        :return:
        '''
        self.backEndDeveloper=backEndDeveloper
        self.backEndLang=backEndLang
        self.frontEndDeveloper=frontEndDeveloper
        self.frontEndLang=frontEndLan
        self.uiTester=uiTester
        self.des=description
        self.res={}

    def _runTest(self):
        print u'我正在执行，相关测试结果需要在这里赋值'
        res={}
        #1 代表执行成功，0代表执行不成功
        res['res']=1
        res['backEndDeveloper']=self.backEndDeveloper
        res['backEndLang']=self.backEndLang
        res['frontEndDeveloper']=self.frontEndDeveloper
        res['frontEndLang']=self.frontEndLang
        res['uiTester']=self.uiTester
        res['traceBack']=None
        res['failPicDir']=None
        #执行过程中需要返回的错误信息
        res['detail']=None
        #初始化的描述信息
        res['des']=self.des
        self.res=res
        #print self.res

    def getRes(self):
        '''
        规定所有测试类的getRes的返回值必须包含以下参数
        即子类中不管使用什么方法，都要返回正确的res格式
        :return:
        '''
        #print u'getRes在执行'
        self._runTest()
        return json.dumps(self.res)

#uiTest为在每一个测试脚本中必须包含的TestBase实例
uiTest=TestBase()