from pydantic import UUID4, BaseModel, Field

from app.enums import BreweryType


class BreweryApiResponse(BaseModel):
    id: UUID4
    name: str
    brewery_type: BreweryType
    address_1: str | None = Field(default=None)
    address_2: str | None = Field(default=None)
    address_3: str | None = Field(default=None)
    city: str
    state_province: str
    postal_code: str
    country: str
    longitude: str | None = Field(default=None)
    latitude: str | None = Field(default=None)
    phone: str | None = Field(default=None)
    website_url: str | None = Field(default=None)
    state: str
    street: str | None = Field(default=None)
