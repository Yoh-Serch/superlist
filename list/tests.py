from django.core.urlresolvers import resolve
from django.test import TestCase
from django.test import HttpRequest
from list.views import home_page

class SmokeTest(TestCase):
    
    def test_root_url_resolves_to_home__page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists </title>', response.title)
        self.assertTrue(response.content.endswith(b'</html>'))
