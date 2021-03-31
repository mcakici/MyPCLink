from django.test import TestCase
from django.test import Client
from django.urls import reverse
from pc_calculator.models import *

#reverse('pc-calc:upload')

class UploadViewLoggedInTest(TestCase):

    def test_logged_out_user_access(self):
        response = self.client.get(reverse('pc-calc:upload'))
        self.assertRedirects(response, '/accounts/login/?next=/upload/', status_code=302)


    def test_logged_in_user_access(self):
        User.objects.create_user('testuser', 'testuser@gmail.com', '123456a.')
        self.client.login(username='testuser', password='123456a.')

        response = self.client.get(reverse('pc-calc:upload'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hi testuser')
