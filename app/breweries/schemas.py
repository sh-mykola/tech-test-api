from pydantic import BaseModel

from app.enums import BreweryType


class BreweryCreateRequest(BaseModel):
    name: str
    brewery_type: BreweryType
    address_1: str
    city: str
    state_province: str
    postal_code: str
    country: str
    longitude: str
    latitude: str
    phone: str
    website_url: str
    state: str
    street: str
