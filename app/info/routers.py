from typing import Annotated

from fastapi import APIRouter, Depends, Path

from app import setup_logger
from app.dependencies import get_brewery_service
from app.infra.services.brewery import BreweryService
from app.infra.services.schemas import BreweryApiResponse

router = APIRouter()
logger = setup_logger(__file__)


@router.get(
    path="/random/breweries/{size}",
    summary="Get random breweries",
    response_model=list[BreweryApiResponse],
)
async def get_data(
    brewery_service: Annotated[BreweryService, Depends(get_brewery_service)], size: int = Path(..., ge=1, le=50)
):
    return brewery_service.get_random_breweries(size)
