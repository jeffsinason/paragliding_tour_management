from sqlalchemy import Column, Integer, String, Float, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database.db import Base

class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True)
    resource_type = Column(String, index=True)  # Vehicle, Driver, Coach, Equipment
    resource_name = Column(String, index=True)  # Name or identifier
    default_availability = Column(String)  # General availability (e.g., Weekdays)
    cost_per_unit = Column(Float)  # Associated cost (e.g., daily rate)
    cost_unit_type = Column(String)  # Per Hour, Per Day, etc.
    details = Column(Text, nullable=True)  # JSON or text for specific details

    availabilities = relationship("ResourceAvailability", back_populates="resource")

 