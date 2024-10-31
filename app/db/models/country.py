from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class Country(Base):
    __tablename__ = 'countries'  # noqa
    country_id = Column(Integer, primary_key=True)
    country_name = Column(String, nullable=True)

    city = relationship("City", back_populates="country")
