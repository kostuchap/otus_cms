
import importlib
import pkgutil

from core.component import Component
from core.ioc import IoC

plugins_path = "plugins"

def load_plugins():
    for _, module_name, _ in pkgutil.iter_modules([plugins_path]):
        module = importlib.import_module(f"{plugins_path}.{module_name}")
        for attr_name in dir(module):
            attr = getattr(module, attr_name)
            if isinstance(attr, type) and issubclass(attr, Component):
                IoC.resolve('IoC.Register', attr_name, attr).execute()
