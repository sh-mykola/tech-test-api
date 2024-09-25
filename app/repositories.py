from pydantic import UUID4

from app.enums import BreweryType
from app.infra.databases.models import BreweryDBModel
from app.infra.databases.postgres import PostgresDatabase
from app.models import Brewery


class BaseRepository:
    pass


class BreweryRepository(BaseRepository):
    def __init__(self, postgres_database: PostgresDatabase):
        self.postgres_database = postgres_database
        self.model = BreweryDBModel

    def __map_db_to_entity(self, db_model: BreweryDBModel) -> Brewery:
        return Brewery(
            id=db_model.id,
            name=db_model.name,
            brewery_type=BreweryType(db_model.brewery_type),
            address_1=db_model.address_1,
            city=db_model.city,
            state_province=db_model.state_province,
            postal_code=db_model.postal_code,
            country=db_model.country,
            longitude=db_model.longitude,
            latitude=db_model.latitude,
            phone=db_model.phone,
            website_url=db_model.website_url,
            state=db_model.state,
            street=db_model.street,
        )

    def __map_entity_to_db(self, entity: Brewery) -> BreweryDBModel:
        return BreweryDBModel(
            id=entity.id,
            name=entity.name,
            brewery_type=entity.brewery_type,
            address_1=entity.address_1,
            city=entity.city,
            state_province=entity.state_province,
            postal_code=entity.postal_code,
            country=entity.country,
            longitude=entity.longitude,
            latitude=entity.latitude,
            phone=entity.phone,
            website_url=entity.website_url,
            state=entity.state,
            street=entity.street,
        )

    def find(self, brewery_id: UUID4) -> Brewery | None:
        with self.postgres_database.get_session() as session:
            db_model = session.query(self.model).filter(self.model.id == brewery_id).first()
            return self.__map_db_to_entity(db_model) if db_model else None

    def find_all(self) -> list[Brewery]:
        with self.postgres_database.get_session() as session:
            db_models = session.query(self.model).all()
            return [self.__map_db_to_entity(db_model) for db_model in db_models]

    def save(self, entity: Brewery) -> Brewery:
        with self.postgres_database.get_session() as session:
            db_model = self.__map_entity_to_db(entity)
            session.add(db_model)
            session.commit()
            session.refresh(db_model)
            return self.find(db_model.id)
