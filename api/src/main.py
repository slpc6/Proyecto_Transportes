"""Punto inicial de la aplicacion"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import importlib
import pkgutil
import uvicorn
from dotenv import load_dotenv

from util.path import Path


app = FastAPI(version= "1.0.0",
              title= "Gestion de facturas",
              description= "")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)


for _, module_name, _ in pkgutil.iter_modules([Path.ROUTERS]):
    module = importlib.import_module(f"router.{module_name}")
    if hasattr(module, "router"):
        app.include_router(module.router)


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True)
    load_dotenv()
