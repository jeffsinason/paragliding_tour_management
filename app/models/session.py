from sqlalchemy import Column, Integer, Date, Float
from app.database.db import Base

class Session(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, index=True)  # Session date
    max_capacity = Column(Integer)  # Maximum number of students
    current_bookings = Column(Integer, default=0)  # Current number of bookings
    cost = Column(Float)  # Session cost