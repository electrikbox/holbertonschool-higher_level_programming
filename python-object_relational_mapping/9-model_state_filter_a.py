#!/usr/bin/python3
""" script that lists all State objects that contain the letter a """

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
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

    qr = session.query(State).filter(State.name.like('%a%')).order_by(State.id)

    session.close()

    for state in qr:
        print("{}: {}".format(state.id, state.name))
