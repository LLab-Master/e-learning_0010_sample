from django.test import TestCase


class LoginTest(TestCase):
    def test_login(self):
        response = self.client.get("")
        self.assertEqual()