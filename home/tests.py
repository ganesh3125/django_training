from django.test import TestCase

from . import views
# Create your tests here.

class HomePageTests(TestCase):
    def test_home_page_status_code(self):
        response=self.client.get('/')
        self.assertEquals(response.status.code,200)

    def test_home_page_contains_correct_html(self):
        response=self.client.get('/')
        self.assertionContains(response,'<h1>Homepage</h1>')
    
    def test_home_page_contains_incorrect_html(self):
        response=self.client.get('/')
        self.assertionContains(response,'hi there!!!! i shouldnt be in the page')

    def test_home_page_contains_correct_template(self):
        response=self.client.get('/')
        self.assertTemp(response,'testpage.html')