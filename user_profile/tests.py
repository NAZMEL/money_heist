from django.contrib.auth.hashers import check_password
from unittest.mock import patch
from rest_framework.reverse import reverse
from money_heist.tests import BaseAPITest


class TestProfileViewSet(BaseAPITest):

    def setUp(self):
        self.password = 'test_password'
        self.user = self.create_and_login(password=self.password)
        self.data = {
            "email": "new@email.com",
        }

    def test_get_profile(self):
        resp = self.client.get(reverse('v1:user_profile:profile'))

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['id'], self.user.id)
        self.assertEqual(resp.data['email'], self.user.email)

    def test_get_profile_unauthorized(self):
        self.logout()
        resp = self.client.get(reverse('v1:user_profile:profile'))

        self.assertEqual(resp.status_code, 401)
