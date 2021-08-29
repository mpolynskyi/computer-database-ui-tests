from urllib.parse import urljoin
from seleniumbase import BaseCase
import pytest


@pytest.mark.usefixtures('base_url')
class BaseAction(BaseCase):

    autouse_fixture_names = ["faker", "request"]

    @pytest.fixture(autouse=True)
    def auto_injector_fixture(self, request):
        names = self.autouse_fixture_names
        for name in names:
            setattr(self, name, request.getfixturevalue(name))

    def setUp(self):
        super(BaseAction, self).setUp()
        pass

    def open(self, url):
        return super().open(urljoin(self.base_url, url))

    def assert_text_in_input(self, element, text):
        self.wait_for_element_visible(element)
        assert self.get_attribute(element, 'value') == text
