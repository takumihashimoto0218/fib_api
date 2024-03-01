import unittest
# テストケースクラスを明示的にインポート
from .src.test_fib import FibTestCase
from .api.test_fib_api import FibAPITestCase
from .api.test_errors import ErrorsCase

def suite():
  test_suite = unittest.TestSuite()
  # テストケースクラスを引数に指定
  test_suite.addTest(unittest.makeSuite(FibTestCase))
  test_suite.addTest(unittest.makeSuite(FibAPITestCase))
  test_suite.addTest(unittest.makeSuite(ErrorsCase))
  return test_suite

if __name__ == '__main__':
  # テストスイートを作成し、実行
  mySuite = suite()
  unittest.TextTestRunner(verbosity=2).run(mySuite)