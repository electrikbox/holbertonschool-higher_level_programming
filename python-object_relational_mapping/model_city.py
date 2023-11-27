#!/usr/bin/python3
""" file that contains the class definition of a State """

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
import MySQLdb

Base = declarative_base()


class City(Base):
    """City class"""
    __tablename__ = "cities"

    id = Column(
        Integer,
        unique=True,
        nullable=False,
        primary_key=True,
        autoincrement=True
    )

    name = Column(
        String(128),
        nullable=False
    )

    state_id = Column(
        Integer,
        ForeignKey('states.id'),
        nullable=False,
    )


if __name__ == "__main__":
    database = MySQLdb.connect(
        host="localhost",
        port=3306
    )
