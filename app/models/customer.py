from sqlalchemy import Column, Integer, String, Text
from app.database.db import Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)  # Full name of the customer
    email = Column(String, unique=True, index=True)  # Email address
    phone = Column(String, unique=True)  # Phone number
    address = Column(Text, nullable=True)  # Optional address