from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = 'sqlite:///./fast_car.db'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_session():
    """Create a new database session."""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()