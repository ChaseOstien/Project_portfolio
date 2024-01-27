from os import getenv
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv
from flask import g


load_dotenv()

# connect to database using url in .env file
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
Session = sessionmaker(bind=engine)
Base = declarative_base()

def init_db(app):
    Base.metadata.create_all(engine)

    app.teardown_appcontext(close_db)

    # This function gets the database connection
def get_db():
    if 'db' not in g:
        # store db connection in app context
        g.db = Session()

    return Session()

# This function closes the database connection
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()



