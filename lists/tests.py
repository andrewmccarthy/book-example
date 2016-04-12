from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase

from lists.views import home_page

class TestHomePage:

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        assert found.func == home_page


    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        # If using Django 1.9 add request=request to fix a new problem
        # https://groups.google.com/forum/#!topic/obey-the-testing-goat-book/fwY7ifEWKMU
        # expected_html = render_to_string('home.html', request=request)
        expected_html = render_to_string('home.html')
        assert response.content.decode() == expected_html
