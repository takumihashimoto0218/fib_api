import unittest
from main import app

class FibAPITestCase(unittest.TestCase):
  # テストのセットアップ: テストケース実行前に毎回呼び出される
  def setUp(self):
    self.app = app.test_client()

  # 正の整数がクエリパラメータとして渡された場合のテスト
  def test_get_fib_positive_integer_input(self):
    response = self.app.get('/fib?n=10')
    self.assertEqual(response.status_code, 200)
    self.assertIn('55', response.data.decode('utf-8'))

  # 負の整数がクエリパラメータとして渡された場合のテスト
  def test_get_fib_negative_integer_input(self):
    response = self.app.get('/fib?n=-1')
    self.assertEqual(response.status_code, 400)
    self.assertIn('Bad request', response.data.decode('utf-8'))

  # 整数以外の文字列がクエリパラメータとして渡された場合のテスト
  def test_fib_api_non_integer_input(self):
    response = self.app.get('/fib?n=abc')
    self.assertEqual(response.status_code, 400)
    self.assertIn('Bad request', response.data.decode('utf-8'))

  # 浮動小数点数がクエリパラメータとして渡された場合のテスト
  def test_fib_api_floating_point_input(self):
    response = self.app.get('/fib?n=1.2')
    self.assertEqual(response.status_code, 400)
    self.assertIn('Bad request', response.data.decode('utf-8'))

# このスクリプトが直接実行された場合にunittestのテストランナーを起動
if __name__ == '__main__':
  unittest.main()
