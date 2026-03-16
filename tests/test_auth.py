"""
Authentication Unit Tests
-------------------------
Purpose: Verifies the Auth views using unittest.mock to simulate Supabase API responses.
"""

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from unittest.mock import patch

class AuthTests(APITestCase):

    @patch('apps.users.views.supabase')
    def test_register_user_mocked(self, mock_supabase):
        # Simulate a successful sign_up response
        mock_supabase.auth.sign_up.return_value = {
            "user": {"id": "12345", "email": "test_mock@example.com"},
            "session": None
        }

        url = reverse('register') 
        data = {'email': 'test_mock@example.com', 'password': 'securepassword123'}
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        mock_supabase.auth.sign_up.assert_called_once()

    @patch('apps.users.views.supabase')
    def test_login_user_mocked(self, mock_supabase):
        # Simulate a successful sign_in response with a JWT token
        mock_supabase.auth.sign_in_with_password.return_value = {
            "user": {"id": "12345", "email": "test_mock@example.com"},
            "session": {"access_token": "fake-jwt-token"}
        }

        url = reverse('login')
        data = {'email': 'test_mock@example.com', 'password': 'securepassword123'}
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access_token', response.data['session'])