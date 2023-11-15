import unittest
from app import app
from config import get_config

class TestApp(unittest.TestCase):

    def setUp(self):
        config = get_config('testing')
        app.config.from_object(config)
        self.app = app.test_client()

    def test_rota_de_login(self):
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)  # Verifica se a rota /login retorna o código 200 OK

    def test_rota_desconhecida(self):
        response = self.app.get('/rota_inexistente')
        self.assertEqual(response.status_code, 404)  # Verifica se uma rota inexistente retorna o código 404 Not Found

if __name__ == '__main__':
    unittest.main()
