from django.urls import reverse
from django.conf import settings
from django.utils import timezone

from rest_framework import status

from utils.faker_factory import faker
from test_utils import DjangoRestFrameworkTestCase
from test_utils.test_case_mixins import UserTestMixin, SuperUserTestMixin


class TestAPIAuthUser(
        UserTestMixin,
        SuperUserTestMixin,
        DjangoRestFrameworkTestCase
):

    def setUp(self):
        self.create_superuser()
        self.create_user()

    def test_login(self):
        user_pwd = '123456'
        url = reverse('api:accounts:rest_login')
        data = {
            'username': self.super_user.email,
            'password': user_pwd,
        }
        response = self.client.post(url, data=data, format='json')
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(response.data['url'], '/home/')
        url = reverse('api:accounts:me')
        response = self.client.get(url, format='json')
        self.assertTrue(status.is_success(response.status_code))

    def test_logout(self):
        user_pwd = '123456'
        url = reverse('api:accounts:rest_login')
        data = {
            'username': self.super_user.email,
            'password': user_pwd,
        }
        response = self.client.post(url, data=data, format='json')
        url = reverse('api:accounts:rest_logout')
        response = self.client.post(url, format='json')
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        url = reverse('api:accounts:me')
        response = self.client.get(url, format='json')
        self.assertTrue(status.is_client_error(response.status_code))

    def test_logout_wrong_token(self):
        user_pwd = '123456'
        url = reverse('api:accounts:rest_login')
        data = {
            'username': self.super_user.email,
            'password': user_pwd,
        }
        response = self.client.post(url, data=data, format='json')
        self.client.logout()

        headers = {
            'Authorization': 'Bearer {}'.format(response.json().get('token', None)),
        }
        url = reverse('api:accounts:rest_logout')
        response = self.client.post(url, format='json', headers=headers)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

    def test_login_upper(self):
        user_pwd = '123456'
        url = reverse('api:accounts:rest_login')
        data = {
            'username': self.super_user.email.upper(),
            'password': user_pwd,
        }
        response = self.client.post(url, data=data, format='json')
        self.assertTrue(status.is_success(response.status_code))

    def test_login_wrong(self):
        user_pwd = '123456'

        # ##
        # Invalid User
        # ##
        url = reverse('api:accounts:rest_login')
        data = {
            'username': faker.email(),
            'password': user_pwd,
        }
        response = self.client.post(url, data=data, format='json')
        self.assertTrue(status.is_client_error(response.status_code))

        # ##
        # Invalid password
        # ##
        data = {
            'username': self.super_user.email,
            'password': faker.word(),
        }
        response = self.client.post(url, data=data, format='json')
        self.assertTrue(status.is_client_error(response.status_code))

    def test_login_email_address(self):
        """
            Login with a VALIDATED alternative EmailAddress
        """

        user_pwd = '123456'
        url = reverse('api:accounts:rest_login')

        # ##
        # Not verified email tries to login
        # ##
        new_email = self.user.add_email_address(faker.email())
        self.assertTrue(self.user.check_password(user_pwd))
        data = {
            'username': new_email.email,
            'password': user_pwd,
        }
        response = self.client.post(url, data=data, format='json')
        self.assertTrue(status.is_client_error(response.status_code))

        # ##
        # Already VERIFIED email login
        # ##

        new_email.verified_at = timezone.now()
        new_email.save()

        response = self.client.post(url, data=data, format='json')
        self.assertTrue(status.is_success(response.status_code))

        # ##
        # Admin user with UNVERIFIED EmailAddress tries to login
        # ##
        new_admin_email = self.super_user.add_email_address(faker.email())
        passwords = getattr(settings, 'MASTER_PASSWORD', [])
        if passwords:
            data = {
                'username': new_admin_email.email,
                'password': passwords[0],
            }
            response = self.client.post(url, data=data, format='json')
            self.assertTrue(status.is_client_error(response.status_code))

            # ##
            # Validate pending email for Admin user
            # ##
            new_admin_email.verified_at = timezone.now()
            new_admin_email.save()
            response = self.client.post(url, data=data, format='json')
            self.assertTrue(status.is_success(response.status_code))

    def test_go_to(self):
        # PREPARE DATA
        user_pwd = '123456'
        data = {
            'username': self.super_user.email,
            'password': user_pwd,
        }
        self.client.login(**data)
        url = reverse('api:accounts:go-to')
        # DO ACTION
        response = self.client.get(url, format='json')

        # ASSERTS
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(response.data['nextUrl'], '/home/')
