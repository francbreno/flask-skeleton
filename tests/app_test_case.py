import unittest
import os
import json
from app import create_app, db

class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client

        # Preparar os dados

    def tearDown(self):
        # limpar os dados
        pass

    def test_deve_listar_usuarios(self):
        # Given
        
        #When
        response = self.client().get('/api/users')
        #Then
        self.assertEquals(200, response.status_code)

        pass

    def test_deve_criar_usuario(self):
        pass

    def test_dev_obter_usuario_por_id(self):
        pass

if __name__ == '__main__':
    unittest.main()