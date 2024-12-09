from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL for SQLite3 during development
SQLALCHEMY_DATABASE_URL = "sqlite:///./paragliding_tours.db"

# Create the SQLAlchemy engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# SessionLocal: To handle sessions for database operations
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base: Used to define the models
Base = declarative_base()