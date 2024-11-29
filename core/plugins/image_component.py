from core.component import Component


class ImageComponent(Component):
    def render(self, params: dict) -> str:
        return f"<img src='{params['url']}' alt='{params['alt']}'>"
