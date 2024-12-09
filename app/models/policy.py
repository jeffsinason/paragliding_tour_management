from sqlalchemy import Column, Integer, String, Text, Boolean, Date
from app.database.db import Base

class Policy(Base):
    __tablename__ = "policies"

    id = Column(Integer, primary_key=True, index=True)
    policy_type = Column(String, index=True)  # Cancellation, Payment, etc.
    policy_text = Column(Text)  # Full policy description
    applies_to = Column(String)  # Group_Tour, XC_Coaching, or Both
    customer_visible = Column(Boolean, default=True)  # Visibility flag
    effective_date = Column(Date, nullable=False)  # Start date for policy
    last_updated = Column(Date, nullable=True)  # Last modification date
    admin_notes = Column(Text, nullable=True)  # Internal notes