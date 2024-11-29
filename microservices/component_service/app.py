import uvicorn
from fastapi import FastAPI, HTTPException
from models.models import ComponentConfig

app = FastAPI(
    title="Component service",
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
)

components = []


@app.get("/components")
async def get_components():
    return components


@app.post("/components")
async def create_component(component: ComponentConfig):
    components.append(component)
    return component


@app.get("/components/{component_type}")
async def get_component_by_type(component_type: str):
    for component in components:
        if component.component_type == component_type:
            return component
    raise HTTPException(status_code=404, detail="Component not found")


# if __name__ == '__main__':
#     uvicorn.run(
#         'app:app',
#         host='0.0.0.0',
#         port=5001,
#     )
