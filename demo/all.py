import os
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
from unittest import runner


print(1111,os.getcwd())
if __name__ == '__main__':
    suite = unittest.TestSuite()

    testcases = unittest.defaultTestLoader.discover(os.getcwd(),"*.py")
    suite.addTest(testcases)

    nowtime = time.strftime("%Y-%m-%d %H-%M-%S",time.localtime())
    name = open(os.getcwd()+'/'+nowtime +'report.html','wb')

    # 参数说明
    HTMLTestRunner(stream=name, verbosity=2, title=u"小水滴测试报告", description=u"差点害死用例").run(suite)
    # unittest.TextTestRunner(verbosity=2).run(suite)
    name.close()