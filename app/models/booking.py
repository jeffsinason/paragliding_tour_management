from sqlalchemy import Column, Integer, String, Float, Date, Text
from app.database.db import Base

class UnifiedBooking(Base):
    __tablename__ = "unified_bookings"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, index=True)  # Links to Customers table
    service_type = Column(String, index=True)  # Group_Tour or XC_Coaching
    service_id = Column(Integer)  # Links to specific service (Tour or Session)
    booking_status = Column(String)  # Confirmed, Pending, or Cancelled
    total_price = Column(Float)  # Total booking cost
    payment_status = Column(String)  # Paid, Partially Paid, or Pending
    start_date = Column(Date, nullable=True)  # Start date for tours
    end_date = Column(Date, nullable=True)  # End date for tours
    selected_dates = Column(Text, nullable=True)  # JSON or string for XC Coaching
    additional_details = Column(Text, nullable=True)  # JSON or text for custom details