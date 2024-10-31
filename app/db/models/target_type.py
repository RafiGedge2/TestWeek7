from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class TargetType(Base):
    __tablename__ = 'targettypes'  # noqa
    target_type_id = Column(Integer, primary_key=True)
    target_type_name = Column(String, nullable=True)

    target = relationship('Target', back_populates='target_type')
