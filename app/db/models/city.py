from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class City(Base):
    __tablename__ = 'cities'  # noqa
    city_id = Column(Integer, primary_key=True)
    city_name = Column(String, nullable=True)
    country_id = Column(Integer, ForeignKey('country.country_id'), nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    target = relationship('Target', back_populates='city')
    country = relationship('Country', lazy='immediate', back_populates='city')
