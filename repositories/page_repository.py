from models.models import Page


class PageRepository:
    def __init__(self):
        self.pages = {}

    def save_page(self, page: Page):
        self.pages[page.id] = page

    def get_page(self, page_id: int) -> Page:
        return self.pages.get(page_id)

    def update_page(self, page: Page):
        if page.id in self.pages:
            self.pages[page.id] = page
        else:
            raise ValueError(f"Page with id {page.id} does not exist")

    def delete_page(self, page_id: int):
        if page_id in self.pages:
            del self.pages[page_id]
        else:
            raise ValueError(f"Page with id {page_id} does not exist")