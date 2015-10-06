#coding=utf-8
'''
运招标的数据，包含工序名，登录用户有关等信息
'''
__author__ = 'xiyuanbupt'
#消息页面中新建任务的对应工序
messageProcessNameList=(u'01: 项目信息',u'02: 项目登记',u'03: 代理协议',u'04: 招标准备',u'05: 网络备案',
                 u'06: 现场备案',u'07: 招标公告',u'08: 接受报名',u'09: 招标文件',
                 u'10: 招标控制价及工程量清单',u'11: 招标文件购买',
                 u'12: 犯罪查询',u'13: 预约开标室',u'14: 投标保证金',
                 u'15: 开标文件准备',u'16: 借支开标款',u'17: 开标',
                 u'18: 预中标公示',u'19: 开评标还款',
                 u'20: 预收服务费',u'21: 评标资料领取',u'22: 备案文件准备',
                 u'23: 服务费及退保证金',u'24: 发票领用',
                 u'25: 评标报告备案',u'26: 备案文件分发',u'27: 存档',
                 u'28: 代收履约保证金',u'29: 履约保证金退款',
                 u'30: 项目结束')

nameToCount={u'刘兆君':'liuzhaojun@164.com',u'陈桂英':'chenguiying@163.com',
             u'王兵鑫':'wangbingxin@163.com',u'郭帅':'guoshuai@163.com',
             u'马双双':'mashuangshuang@163.com',u'关西成':'guanxicheng@163.com',
             u'季丽娜':'jilina@163.com',u'梁冰':'liangbing@163.com',
             u'李雪':'lixue@163.com',u'金婷婷':'jintingting@163.com',
             u'张莹':'zhangying@163.com',u'鲍吉龙':'baojilong@163.com',
             u'徐潇然':'xuxiaoran@163.com',u'张满':'zhangman@163.com',
             u'郭长全':'guochangquan@163.com',u'赵青松':u'zhaoqingsong@163.com'}
if __name__=="__main__":
    for i in messageProcessNameList:
        print i
    for key in nameToCount:
        print key,nameToCount[key]
    from LoginPage import LoginPage
    from selenium import webdriver
    print u'单元测试未进行'
    driver=webdriver.Firefox()
    loginPage=LoginPage(driver)
    for key in nameToCount:
        loginPage.login(nameToCount[key],'test')
        res=loginPage.verifiLogin()
        if res==u'':
            print u'%s登录失败'%key
            print u'当前的cookies为'
            print driver.get_cookies()
        else:
            print u'%s登录成功'%key
            print u'当前的cookies为'
            print driver.get_cookies()

