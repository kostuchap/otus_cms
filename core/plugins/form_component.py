from core.component import Component


class FormComponent(Component):
    def render(self, params: dict) -> str:
        form = "<form>"
        for field in params['fields']:
            form += f"<input type='{field['type']}' name='{field['name']}'>"
        form += "</form>"
        return form
