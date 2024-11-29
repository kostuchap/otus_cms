from pydantic import BaseModel
from typing import List, Dict, Any


class ComponentConfig(BaseModel):
    component_type: str
    params: Dict[str, Any]


class Page(BaseModel):
    id: int
    components: List[ComponentConfig]
