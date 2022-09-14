import os
import unittest

if __name__ == '__main__':
    suite = unittest.TestSuite()
    testcases = unittest.defaultTestLoader.discover(os.getcwd(),"*.py")
    suite.addTest(testcases)
    unittest.TextTestRunner(verbosity=2).run(suite)