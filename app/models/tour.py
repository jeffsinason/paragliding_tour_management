from sqlalchemy import Column, Integer, String, Date, Float
from app.database.db import Base

class Tour(Base):
    __tablename__ = "tours"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)  # Tour name
    start_date = Column(Date)  # Tour start date
    end_date = Column(Date)  # Tour end date
    max_capacity = Column(Integer)  # Maximum number of customers
    current_bookings = Column(Integer, default=0)  # Current number of bookings
    cost = Column(Float)  # Tour cost