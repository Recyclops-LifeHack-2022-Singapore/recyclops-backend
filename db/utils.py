import argparse
import sys
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import Base, Item
from seed import seeds

@contextmanager
def init_db_connection():
    engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
    try:
        yield engine
    finally:
        # do nothing, session will be closed on exiting this context
        engine.dispose()


def create_db(engine):
    Base.metadata.create_all(engine)


def seed_db(engine):
    with Session(bind=engine) as session:
        for obj in seeds():
            session.add(obj)

        session.commit()


def clean_db(engine):
    for tbl in reversed(Base.metadata.sorted_tables):
        engine.execute(tbl.delete())


def drop_db(engine):
    Base.metadata.drop_all(engine)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # possible db actions
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-c', '--create', action='store_true', help='create a new database and loads the schema')
    group.add_argument('-s', '--seed', action='store_true', help='seeds data from seed.py')
    group.add_argument('-cl', '--clean',  action='store_true', help='delete all records in database')
    group.add_argument('-d', '--drop',  action='store_true', help='drops the current database')

    group.add_argument('-t', '--test',  action='store_true') # TODO: REMOVE 

    args = parser.parse_args()

    with init_db_connection() as engine:
        if args.create: # create db and loads schema
            create_db(engine)

        elif args.seed: # seed / populates the db
            seed_db(engine)

        elif args.clean: # empty tables
            clean_db(engine)

        elif args.drop: # drop db
            drop_db(engine)

        elif args.test:
            create_db(engine)
            seed_db(engine)

            with Session(bind=engine) as session:
                values = session.query(Item).all()
                print(values)

        else:
            print("Unknown action requested, cannot proceed")
            sys.exit(1)
