import uvicorn
from fastapi import FastAPI, HTTPException

from core.component import Component
from core.load_plugins import load_plugins
from core.middleware import component_middleware
from models.models import Page, ComponentConfig
from core.page_controller import PageController
import requests
from fastapi.responses import HTMLResponse
from core.ioc import IoC
import importlib
import pkgutil
import os

from repositories.page_repository import PageRepository


app = FastAPI(
    title="Generate page",
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
)

# Регистрируем middleware
# app.middleware("http")(component_middleware)

load_plugins()

page_controller = PageController()

page_repository = PageRepository()

@app.post("/pages", response_model=Page)
async def save_page(page: Page):
    page_repository.save_page(page)
    return page

@app.put("/pages/{page_id}", response_model=Page)
async def update_page(page_id: int, page: Page):
    page.id = page_id
    page_repository.update_page(page)
    return page

@app.get("/pages/{page_id}", response_model=Page)
async def get_page(page_id: int):
    page = page_repository.get_page(page_id)
    if page is None:
        raise HTTPException(status_code=404, detail="Page not found")
    return page

@app.delete("/pages/{page_id}")
async def delete_page(page_id: int):
    page_repository.delete_page(page_id)
    return {"message": "Page deleted"}

@app.post("/generate_page", response_class=HTMLResponse)
async def generate_page(page_config: Page):
    return HTMLResponse(content=page_controller.generate_page(page_config))

@app.get("/generate_page/{page_id}", response_class=HTMLResponse)
async def generate_page_by_id(page_id: int):
    page = page_repository.get_page(page_id)
    return HTMLResponse(content=page_controller.generate_page(page))


#
# if __name__ == '__main__':
#     uvicorn.run(
#         'app:app',
#         host='0.0.0.0',
#         port=5051,
#     )
