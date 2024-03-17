#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
import State and Base from model_state-
from model_state import Base, State
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@loclahost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    Session = Session()
    for state in Session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
    Session.close()
