#coding=utf-8
import unittest
from configparser import ConfigParser

from selenium import webdriver

from regressionScript import *

#定义全局变量
cfg=ConfigParser()
cfg.read('zhaobiao.ini')
_=cfg.get('browser','client')
_='webdriver.%s'%(_)
_=eval(_)
driver=_()

if __name__=="__main__":
    unittest.main()