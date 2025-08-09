from django.test import TestCase
from .models import Child
from django.urls import reverse

class ChildModelTest(TestCase):
    def test_string_representetion(self):
        child = Child(Full_name="john doe", )
        self.assertEqual(str(child), child.Full_name)

class ViewTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome to Mwaami Faundation')
    def test_redirect_view_status_code(self):
        url = reverse('redirect_to_home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        