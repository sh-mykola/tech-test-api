from importlib import import_module
from pkgutil import iter_modules
from sys import modules

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.breweries.routers import router as data_router
from app.logger import setup_logger

logger = setup_logger(__file__)


def create_app() -> FastAPI:
    """Factory that initializes FastApi application"""

    app = FastAPI(
        title="TechTestAPI v1",
        description="Here you will able to discover all of the ways you can interact with the TechTestAPI.",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost",
            "http://localhost:8025",
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get(path="/ping")
    def ping():
        return "pong"

    for _, module_name, _ in iter_modules(__path__):
        module_path = f"{__name__}.{module_name}.routers"

        try:
            import_module(module_path)
        except ModuleNotFoundError:
            continue

        module = modules[module_path]
        router = getattr(module, "router")

        logger.info(f"Registering router for {module_name}")

        app.include_router(router=router, prefix=f"/{module_name}", tags=[module_name])

    return app
