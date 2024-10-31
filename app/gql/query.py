from graphene import ObjectType, Field, Int, Date, List, String
from app.db.database import session_maker
from app.db.models import Mission, City, Country, Target
from app.gql.types.mission_type import MissionType


class Query(ObjectType):
    mission_by_id = Field(MissionType, mission_id=Int(required=True))
    mission_by_date_range = List(MissionType, start_date=Date(required=True), end_date=Date(required=True))
    mission_by_country = List(MissionType, country=String(required=True))

    @staticmethod
    def resolve_mission_by_id(root, info, mission_id):
        with session_maker() as session:
            return session.query(Mission).get(mission_id)

    @staticmethod
    def resolve_mission_by_date_range(root, info, start_date, end_date):
        with session_maker() as session:
            return session.query(Mission).filter(Mission.mission_date.between(start_date, end_date))

    @staticmethod
    def resolve_mission_by_country(root, info, country):
        with session_maker() as session:
            targets = (
                session.query(Target.mission_id)
                .join(City, Target.city_id == City.city_id)
                .join(Country, City.country_id == Country.country_id)
                .filter(Country.country_name == country)
                .subquery()
            )
            return session.query(Mission).filter(Mission.mission_id.in_(targets)).all()

