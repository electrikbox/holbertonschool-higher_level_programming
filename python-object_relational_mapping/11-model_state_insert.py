#!/usr/bin/python3
""" script that prints the State object with the name passed as argument """

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

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    print(new_state.id)

    session.close()
