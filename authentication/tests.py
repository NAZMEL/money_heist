from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from money_heist.tests import BaseAPITest
from money_heist import user_data                  # in base directory


class TestObtainTokenPair(BaseAPITest):

    def setUp(self):
        self.email = user_data.user_email
        self.password = user_data.user_password
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
        self.email = user_data.user_email
        self.password = user_data.user_password
        self.user = self.create(self.email, self.password)
        self.refresh_token = str(RefreshToken.for_user(self.user))

    def test_get_access_token(self):
        response = self.client.post(reverse('v1:authentication:refresh'), data = {'refresh': self.refresh_token})
        self.assertIn('access', response.data)

    def test_get_token_refresh_error(self):
        response = self.client.post(reverse('v1:authentication:refresh'), data={'refresh': 'fail_data'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)