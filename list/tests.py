from django.core.urlresolvers import resolve
from django.test import TestCase
from list.views import home_page

class SmokeTest(TestCase):
    
    def test_root_url_resolves_to_home__page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
