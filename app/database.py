from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL for MySQL
DATABASE_URL = "mysql+pymysql://username:password@localhost/mydatabase"

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all models
Base = declarative_base()

def get_db():
    """
    Dependency to get a DB session.
    Yields a new session and closes it after the request is done.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()