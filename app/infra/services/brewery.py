import requests
from pydantic.v1 import ValidationError

from app.infra.services.schemas import BreweryApiResponse
from app.logger import setup_logger

logger = setup_logger(__file__)


class BreweryService:
    def __init__(self, brewery_url):
        self.brewery_url = brewery_url

    def get_random_breweries(self, size: int = 1) -> list[BreweryApiResponse]:

        logger.info(f"Getting {size} random breweries")

        response = requests.get(f"{self.brewery_url}/breweries/random?size={size}")

        if response.status_code != 200:
            logger.error(f"Error while fetching breweries: {response.text}")
            raise Exception(f"Error while fetching breweries: {response.text}")

        try:
            result = [BreweryApiResponse(**brewery) for brewery in response.json()]
        except ValidationError as e:
            logger.error(f"Error while parsing breweries: {e}")
            raise Exception(f"Error while parsing breweries: {e}")

        logger.info(f"Successfully fetched {size} random breweries")
        return result
