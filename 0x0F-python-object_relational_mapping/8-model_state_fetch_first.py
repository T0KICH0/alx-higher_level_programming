#!/usr/bin/python3
"""Prints the first state obj, takes 3 args"""


if __name__ == "__main__":
    from sys import argv
    from model_state import State, Base
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    engin = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engin)
    Session = sessionmaker(bind=engin)
    st = Session().query(State).first()
    if st:
        print("{}: {}".format(st.id, st.name))
    else:
        print("Nothing")
    session().close()
