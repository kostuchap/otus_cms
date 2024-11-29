from core.component import Component


class TextComponent(Component):
    def render(self, params: dict) -> str:
        return f"<p>{params['text']}</p>"
