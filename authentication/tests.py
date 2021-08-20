from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status
import secrets


class TestObtainTokenPair(APITestCase):

    def setUp(self):
        self.email = "test@test.com"
        self.password = "qwerty12345"
        self.user = User.objects.create_user(self.email, self.password)
        self.user.is_active = True
        self.user.save()

    def test_auth(self):
        data = {"email": self.email, "password": self.password}
        response = self.client.post(reverse("v1:authentication:obtain"), data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_auth_wrong_password(self):
        self.fail("Write later")

    def test_auth_wrong_email(self):
        self.fail("Write later")
