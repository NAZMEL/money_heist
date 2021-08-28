from rest_framework import status
from rest_framework.reverse import reverse

from authentication.models import User
from money_heist.tests import BaseAPITest


class TestProfileViewSet(BaseAPITest):

    def setUp(self):
        self.email = 'test_email@gmail.com'
        self.password = 'test_password'
        self.user = self.create_and_login(email=self.email, password=self.password)

    def test_get_profile_info(self):
        response = self.client.get(reverse('v1:user_profile:user_info'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_profile_info_when_user_is_not_active(self):
        user = User.objects.get(email=self.user.email)
        user.is_active = False
        user.save()

        response = self.client.get(reverse('v1:user_profile:user_info'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TestUpdateProfileView(BaseAPITest):

    def setUp(self):
        self.email = 'test_email@gmail.com'
        self.password = 'test_password'
        self.user = self.create_and_login(email=self.email, password=self.password)

    def test_change_email_user_success(self):
        data = {
            'email': 'new_email@gmail.com',
            'password': self.password
        }
        response = self.client.patch(reverse('v1:user_profile:change_email', args=(self.user.id, )), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_change_email_another_user(self):
        another_user = self.create(
            email='another_email@gmail.com',
            password='another_password'
        )
        data = {
            'email': 'new_email@gmail.com',
            'password': self.password
        }
        response = self.client.patch(reverse('v1:user_profile:change_email', args=(another_user.id,)), data=data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_change_email_with_incorrect_data(self):
        data = {
            'email': None,
            'password': self.password
        }
        response = self.client.patch(reverse('v1:user_profile:change_email', args=(self.user.id,)), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestChangePasswordView(BaseAPITest):

    def setUp(self):
        self.email = 'test_email@gmail.com'
        self.password = 'test_password'
        self.user = self.create_and_login(email=self.email, password=self.password)

    def test_change_password_user_success(self):
        data = {
            'email': self.email,
            'password': 'new_password'
        }
        response = self.client.patch(reverse('v1:user_profile:change_email', args=(self.user.id, )), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_change_password_with_incorrect_data(self):
        data = {
            'email': self.email,
            'password': None
        }
        response = self.client.patch(reverse('v1:user_profile:change_email', args=(self.user.id,)), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


