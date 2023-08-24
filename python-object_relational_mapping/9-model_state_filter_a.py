'''A script that lists all states'''

if __name__ == '__main__':
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    if len(argv) != 4:
        print('error')
    else:
        user = argv[1]
        password = argv[2]
        db_name = argv[3]
        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(user, password, db_name),
            pool_pre_ping=True,
        )
        Session = sessionmaker(bind=engine)
        session = Session()
        for states in session.query(State).filter(State.name.like('%a%')):
            print('{}: {}'.format(states.id, states.name))
