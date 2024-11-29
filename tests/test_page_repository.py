import unittest
from models.models import Page, ComponentConfig
from repositories.page_repository import PageRepository


class TestPageRepository(unittest.TestCase):

    def setUp(self):
        self.repo = PageRepository()

    def test_save_page(self):
        page = Page(id=1, components=[])
        self.repo.save_page(page)
        self.assertEqual(self.repo.pages[1], page)

    def test_get_page(self):
        page = Page(id=1, components=[])
        self.repo.save_page(page)
        retrieved_page = self.repo.get_page(1)
        self.assertEqual(retrieved_page, page)

    def test_get_page_not_found(self):
        retrieved_page = self.repo.get_page(1)
        self.assertIsNone(retrieved_page)

    def test_update_page(self):
        page = Page(id=1, components=[])
        self.repo.save_page(page)
        updated_page = Page(id=1, components=[ComponentConfig(component_type="component1", params={})])
        self.repo.update_page(updated_page)

        self.assertEqual(self.repo.pages[1], updated_page)

    def test_update_page_not_found(self):
        page = Page(id=1, components=[])

        with self.assertRaises(ValueError):
            self.repo.update_page(page)

    def test_delete_page(self):
        page = Page(id=1, components=[])
        self.repo.save_page(page)
        self.repo.delete_page(1)
        self.assertNotIn(1, self.repo.pages)

    def test_delete_page_not_found(self):
        with self.assertRaises(ValueError):
            self.repo.delete_page(1)
