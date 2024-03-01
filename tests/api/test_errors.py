import unittest
from src.main import app

class ErrorsCase(unittest.TestCase):
  def setUp(self):
    app.testing = True
    self.client = app.test_client()

  # 存在しないエンドポイントへのアクセステスト
  def test_not_found(self):
    response = self.client.get('/non-existent-endpoint')
    self.assertEqual(response.status_code, 404)
    self.assertIn('Not found', response.data.decode('utf-8'))

if __name__ == '__main__':
  unittest.main()
