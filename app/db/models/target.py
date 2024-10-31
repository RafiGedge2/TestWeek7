from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class Target(Base):
    __tablename__ = 'targets'  # noqa
    target_id = Column(Integer, primary_key=True)
    mission_id = Column(Integer, ForeignKey('mission.mission_id'), nullable=True)
    target_industry = Column(String, nullable=True)
    city_id = Column(Integer, ForeignKey('city.city_id'), nullable=True)
    target_type_id = Column(Integer, ForeignKey('target.target_type_id'), nullable=True)
    target_priority = Column(Integer, nullable=True)

    # mission = relationship('Mission', lazy='immediate', back_populates='target')
    # city = relationship('City', lazy='immediate', back_populates='target')
    # target_type = relationship('TargetType', lazy='immediate', back_populates='target')
