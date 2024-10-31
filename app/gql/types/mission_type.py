from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from app.db.models import Mission


class MissionType(SQLAlchemyObjectType):
    class Meta:
        model = Mission
        interfaces = (relay.Node,)
