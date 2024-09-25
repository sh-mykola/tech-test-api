from typing import Annotated

from fastapi import Depends

from app.configs import settings
from app.infra.databases.postgres import PostgresDatabase
from app.infra.services.brewery import BreweryService
from app.repositories import BreweryRepository


def get_brewery_service() -> BreweryService:
    return BreweryService(brewery_url=settings.BREWERIES_API_URL)


def get_postgres_database() -> PostgresDatabase:
    return PostgresDatabase()


def get_brewery_repository(
    postgres_database: Annotated[PostgresDatabase, Depends(get_postgres_database)]
) -> BreweryRepository:
    return BreweryRepository(
        postgres_database=postgres_database,
    )
