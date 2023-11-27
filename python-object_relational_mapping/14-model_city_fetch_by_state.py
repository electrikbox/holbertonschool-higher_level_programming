#!/usr/bin/python3
""" script that prints all City objects from the database """

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username,
        password,
        database
    ), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(City, State).filter(
        State.id == City.state_id).order_by(City.id).all()

    for city, state in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
