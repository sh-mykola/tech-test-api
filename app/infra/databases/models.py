from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from app.infra.databases.base import Base


class BreweryDBModel(Base):
    __tablename__ = "brewery"

    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String, nullable=False)
    brewery_type = Column(String, nullable=False)
    address_1 = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state_province = Column(String, nullable=False)
    postal_code = Column(String, nullable=False)
    country = Column(String, nullable=False)
    longitude = Column(String, nullable=False)
    latitude = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    website_url = Column(String, nullable=False)
    state = Column(String, nullable=False)
    street = Column(String, nullable=False)
