import unittest
import os
import json
from app import create_app, db

class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()

        db.create_all()

        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        # limpar os dados
        db.session.remove()
        db.drop_all()

        self.app_context.pop()

    def test_get_auth_returns_method_not_allowed(self):
        response = self.client.get('/auth')
        assert 405 == response.status_code

    def test_post_auth_with_invalid_credentials_returns_bad_request(self):
        response = self.client.post(
            '/auth', 
            data={ 'username':'joao', 'password':'123'},
            headers={ 'Content-Type': 'application/json'})

        assert 400 == response.status_code

    def test_register_with_valid_data_returns_created(self):
        response = self.client.post(
            '/api/users/register',
            data={ 'username':'maria', 'password':'abc123'},)
        
        assert 201 == response.status_code

if __name__ == '__main__':
    unittest.main()