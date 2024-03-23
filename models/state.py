#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import sessionmaker, relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship(
            "City", cascade="all, delete-orphan", backref="state")
    type_storage = os.getenv("HBNB_TYPE_STORAGE")
    if type_storage != 'db':
        @property
        def cities(self):
            """
            Getter method to return Cities that are linked to States
            """
            city_objs = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    city_obj.append(city)
            return city_objs
    """
        @property
        def cities(self):
        Session = sessionmaker(bind=Base.metadata.bind)
        with Session() as session:
            cities = session.query(City).filter(City.state_id == self.id).all()
        return cities
    """
