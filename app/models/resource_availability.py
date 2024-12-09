from sqlalchemy import Column, Integer, ForeignKey, String, Date
from sqlalchemy.orm import relationship
from app.database.db import Base

class ResourceAvailability(Base):
    __tablename__ = "resource_availability"

    id = Column(Integer, primary_key=True, index=True)
    resource_id = Column(Integer, ForeignKey("resources.id"), index=True)
    date = Column(Date, index=True)  # Specific date for availability/unavailability
    availability_type = Column(String)  # Available or Unavailable

    resource = relationship("Resource", back_populates="availabilities")