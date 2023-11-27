#!/usr/bin/python3
""" file that contains the class definition of a State """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import MySQLdb

Base = declarative_base()


class State(Base):
    """State class"""
    __tablename__ = "states"

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


if __name__ == "__main__":
    database = MySQLdb.connect(
        host="localhost",
        port=3306
    )
