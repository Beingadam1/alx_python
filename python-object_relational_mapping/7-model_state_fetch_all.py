'''
A script that lists all State objects from a database.
Database to be entered by user.
'''

# import modules
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State

if __name__ == '__main__':
    # arguement supplied by user
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # connect to the database using create_engine
    database = f"mysql+mysqldb://{user}:{password}@localhost:3306/{db_name}"
    engine = create_engine(database)

    # create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # execute query
    states = session.query(State).order_by(State.id).all()

    for item in states:
        print('{}: {}'.format(item.id, item.name))

    # close session
    session.close()
