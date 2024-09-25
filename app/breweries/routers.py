from typing import Annotated

from fastapi import APIRouter, Body, Depends, Path
from pydantic import UUID4

from app import setup_logger
from app.breweries.schemas import BreweryCreateRequest
from app.dependencies import get_brewery_repository
from app.models import Brewery
from app.repositories import BreweryRepository

router = APIRouter()
logger = setup_logger(__file__)


@router.post(
    path="",
    summary="Save a new brewery",
    response_model=Brewery,
)
async def save_data(
    brewery_repository: Annotated[BreweryRepository, Depends(get_brewery_repository)],
    request_model: BreweryCreateRequest = Body(...),
):
    brewery = brewery_repository.save(Brewery(**request_model.model_dump()))

    return brewery


@router.get(
    path="/{brewery_id}",
    summary="Get a brewery by ID",
    response_model=Brewery,
)
async def get_data_one(
    brewery_repository: Annotated[BreweryRepository, Depends(get_brewery_repository)],
    brewery_id: UUID4 = Path(...),
):
    return brewery_repository.find(brewery_id)


@router.get(
    path="",
    summary="Get all breweries",
    response_model=list[Brewery],
)
async def get_data_all(
    brewery_repository: Annotated[BreweryRepository, Depends(get_brewery_repository)],
):
    return brewery_repository.find_all()
