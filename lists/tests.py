from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        """Can we resolve the URL for the home page to a view?"""

        found = resolve("/")
        self.assertEqual(found.func, home_page)


    def test_home_page_returns_correct_html(self):
        """We can reach the homepage, but is the page itself right?"""

        request = HttpRequest()
        response = home_page(request)

        self.assertTrue(response.content.startswith(b"<html>"))
        self.assertIn(b'<title>To-Do Lists</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))