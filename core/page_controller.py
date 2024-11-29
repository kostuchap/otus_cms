import requests
from fastapi import FastAPI

from core.ioc import IoC
from core.load_plugins import load_plugins
from models.models import Page, ComponentConfig

app = FastAPI()


class PageController:

    def __init__(self):
        self.plugins_path = "plugins"

    def generate_page(self, page_config: Page) -> str:
        page = []
        for component_config in page_config.components:
            response = requests.get(f"http://componentservice:5001/components/{component_config.component_type}")
            # response = requests.get(f"http://localhost:5001/components/{component_config.component_type}")

            component_data = response.json()

            for k, v in component_data["params"].items():
                if k in component_config.params:
                    component_data["params"][k] = component_config.params[k]

            component = ComponentConfig(component_type=component_data["component_type"],
                                        params=component_data["params"])
            try:
                component_instance = IoC.resolve(component.component_type)
            except ValueError as e:
                load_plugins()

            component_instance = IoC.resolve(component.component_type)
            page.append(component_instance.render(component.params))

        return ''.join(page)
