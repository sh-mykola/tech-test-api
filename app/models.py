from uuid import uuid4

from pydantic import UUID4, BaseModel, Field

from app.enums import BreweryType


def generate_uuid() -> UUID4:
    return uuid4()


class Brewery(BaseModel):
    id: UUID4 = Field(default_factory=generate_uuid)
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
