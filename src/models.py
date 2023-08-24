import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    favorite_characters = Column(String(250))
    favorite_planet = Column(String(250))
    favorite_vehicle = Column(String(250))

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    favorite_characters = Column(String(250), ForeignKey('characters.name'))
    favorite_planet = Column(String(250), ForeignKey('planet.name'))
    favorite_vehicle = Column(String(250), ForeignKey('vehicle.name'))




class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer)
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    gender = Column(String(250))
    birth_year = Column(Integer)  
    homeworld = Column(String(250))  
    person_id = Column(Integer, ForeignKey('person.id'))
    # person = relationship(Person)


class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250))
    population = Column(Integer)
    terrain = Column(String(250))
    rotation_period = Column(Integer)
    

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250))
    manufacturer = Column(String(250))
    cost_in_credits = Column(Integer)
    passengers = Column(Integer)
    starship_class = Column(String(250))




    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
