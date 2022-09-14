import unittest


class Test01(unittest.TestCase):
    def setUp(self) :
        print("用例开始执行")

    def tearDown(self) :
        print("用例执行结束")

    @classmethod
    def setUpClass(cls):
        print("类开始执行")

    @classmethod
    def tearDownClass(cls) :
        print("类执行结束")