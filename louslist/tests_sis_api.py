from django.test import TestCase
from django.contrib.auth.models import User

class SISAPITests(TestCase):
    def setUp(self):
        credentials = {"username": "test_username", "password": "test_password"}
        self.credentials = credentials
        User.objects.create_user(self.credentials)