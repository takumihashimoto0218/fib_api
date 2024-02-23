import unittest
from main import app, fib

class FibTestCase(unittest.TestCase):
  #テストの初期設定
  def setUp(self):
    self.app = app.test_client()

  # src.mainのfib関数の挙動テスト
  def test_fib(self):
    self.assertEqual(fib(10), 55)
    self.assertEqual(fib(100), 354224848179261915075)
    self.assertRaises(ValueError, fib, -1)

  def test_get_fib_positive_integer_input(self):
    response = self.app.get('/fib?n=10')
    self.assertEqual(response.status_code, 200)
    self.assertIn('55', response.data.decode('utf-8'))

  def test_get_fib_negative_integer_input(self):
    response = self.app.get('/fib?n=-1')
    self.assertEqual(response.status_code, 400)
    self.assertIn('Bad request', response.data.decode('utf-8'))

  def test_fib_api_non_integer_input(self):
    response = self.app.get('/fib?n=abc')
    self.assertEqual(response.status_code, 400)
    self.assertIn('Bad request', response.data.decode('utf-8'))

  def test_not_found(self):
    # 存在しないエンドポイントへのアクセスをテスト
    response = self.app.get('/non-existent-endpoint')
    self.assertEqual(response.status_code, 404)
    self.assertIn('Not found', response.data.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()