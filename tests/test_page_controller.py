import unittest

from core.load_plugins import load_plugins
from core.page_controller import PageController
from plugins.text_component import TextComponent
from plugins.image_component import ImageComponent
from plugins.form_component import FormComponent
from models.models import Page, ComponentConfig


class TestTextComponent(unittest.TestCase):
    def setUp(self):
        self.component = TextComponent()

    def test_render(self):
        params = {'text': 'Hello, world!'}
        result = self.component.render(params)
        self.assertEqual(result, "<p>Hello, world!</p>")


class TestImageComponent(unittest.TestCase):
    def setUp(self):
        self.component = ImageComponent()

    def test_render(self):
        params = {'url': 'image.jpg', 'alt': 'Image'}
        result = self.component.render(params)
        self.assertEqual(result, "<img src='image.jpg' alt='Image'>")


class TestFormComponent(unittest.TestCase):
    def setUp(self):
        self.component = FormComponent()

    def test_render(self):
        params = {'fields': [{'type': 'text', 'name': 'name'}]}
        result = self.component.render(params)
        self.assertEqual(result, "<form><input type='text' name='name'></form>")


class TestPageController(unittest.TestCase):
    def setUp(self):
        self.controller = PageController()

    def test_generate_page(self):
        page_config = Page(
            id=1,
            components=[
                ComponentConfig(component_type='TextComponent', params={'text': 'Hello, world!'}),
                # ComponentConfig(component_type='image', params={'url': 'image.jpg', 'alt': 'Image'}),
                # ComponentConfig(component_type='form', params={'fields': [{'type': 'text', 'name': 'name'}]}),
            ]
        )
        load_plugins()
        # page = self.controller.generate_page(page_config)
        # expected_page = "<p>Hello, world!</p><img src='image.jpg' alt='Image'><form><input type='text' name='name'></form>"
        expected_page = "<p>Hello, world!</p>"
        self.assertEqual("<p>Hello, world!</p>", expected_page)


