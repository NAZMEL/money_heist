from unittest.mock import patch

from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from mixer.backend.django import mixer
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from money_heist import settings
from money_heist.tests import BaseAPITest
from money_heist.tasks import send_email
from .tokens import TokenGenerator
from authentication.models import User


class TestObtainTokenPair(BaseAPITest):

    def setUp(self):
        self.email = 'test_email@gmail.com'
        self.password = 'test_pass'
        self.user = self.create(self.email, self.password)
        self.data = {
            'email': self.email,
            'password': self.password
        }

    def test_auth_get_token_pair(self):
        response = self.client.post(reverse("v1:authentication:obtain"), data=self.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_auth_get_token_error(self):
        fail_data = {
            'email': 'fail_email',
            'password': 'fail_password'
        }
        response = self.client.post(reverse('v1:authentication:obtain'), data=fail_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TestRefreshJSONWebToken(BaseAPITest):

    def setUp(self):
        self.email = 'test_email@gmail.com'
        self.password = 'test_pass'
        self.reverse_url = reverse('v1:authentication:refresh')
        self.user = self.create(self.email, self.password)
        self.refresh_token = str(RefreshToken.for_user(self.user))

    def test_get_access_token_refresh(self):
        response = self.client.post(self.reverse_url, data={'refresh': self.refresh_token})
        self.assertIn('access', response.data)

    def test_get_token_refresh_error(self):
        response = self.client.post(self.reverse_url, data={'refresh': 'fail_data'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)



class TestSignUpView(APITestCase):

    def setUp(self):
        self.email = 'test_email@gmail.com'
        self.password = 'test_password'
        self.reverse_url = reverse('v1:authentication:sign-up')
        self.data = {
            'email': self.email,
            'password': self.password
        }

    def test_user_signup_success(self):
        response = self.client.post(
            self.reverse_url,
            self.data,
            format="json"
        )
        self.assertEqual(response.data['email'], self.data['email'])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_signup_with_bad_request(self):
        response = self.client.post(self.reverse_url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_signup_with_incorrect_email(self):
        data = {
            'email': None,
            'password': 'any_password'
        }
        response = self.client.post(
            self.reverse_url,
            data,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_signup_with_incorrect_password(self):
        # create user
        self.client.post(
            self.reverse_url,
            self.data,
            format="json"
        )
        response = self.client.post(
            reverse('v1:authentication:obtain'),
            data={
                'email': self.email,
                'password': 'another_password'
            },
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_signup_user_exists(self):
        self.client.post(
            self.reverse_url,
            self.data,
            format="json"
        )
        response = self.client.post(
            self.reverse_url,
            self.data,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_cannot_signin_if_he_is_not_active(self):
        user = User.objects.create_user(
            email=self.email,
            password=self.password
        )
        user.save()
        response = self.client.post(
            reverse('v1:authentication:obtain'),
            self.data,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_signin_after_activation(self):
        response = self.client.post(
            self.reverse_url,
            self.data,
            format="json"
        )
        user = User.objects.get(email=self.email)
        user.is_active = True
        user.save()

        response = self.client.post(
            reverse('v1:authentication:obtain'),
            self.data,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestSendEmailCeleryTask(BaseAPITest):

    def setUp(self):
        self.email = 'melnyknasar@gmail.com'
        self.password = 'test_password'
        self.user = mixer.blend(User)
        self.token = f'{urlsafe_base64_encode(force_bytes(self.email))}.{TokenGenerator.make_token(self.user)}'
        self.url = f'{settings.USER_ACTIVATION_URL}?token={self.token}'
        self.context = {
            'url': self.url,
            'email': self.email
        }
        self.template = 'notifications/activate_user.html'

    @patch('money_heist.tasks.send_email.delay')
    def test_success(self, send):

        send_email.delay(
                subject="Activate your MoneyHeist account",
                template=self.template,
                recipients=[self.email],
                context=self.context
        )
        send.assert_called_with()

    # def test_send_email_success(self):
    #     try:
    #         send_email.delay(
    #             subject="Activate your MoneyHeist account",
    #             template=self.template,
    #             recipients=[self.email],
    #             context=self.context
    #         )
    #         status_code = status.HTTP_200_OK
    #     except SoftTimeLimitExceeded as e:
    #         status_code = status.HTTP_424_FAILED_DEPENDENCY
    #     except MaxRetriesExceededError as e:
    #         status_code = status.HTTP_408_REQUEST_TIMEOUT
    #
    #     self.assertEqual(status_code, status.HTTP_200_OK)

