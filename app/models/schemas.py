from pydantic import BaseModel
from typing import Optional
from datetime import date

# --- UnifiedBooking Schemas ---
class UnifiedBookingBase(BaseModel):
    customer_id: int
    service_type: str
    service_id: int
    booking_status: str
    total_price: float
    payment_status: str
    start_date: Optional[date]
    end_date: Optional[date]
    selected_dates: Optional[str]
    additional_details: Optional[str]

class UnifiedBookingCreate(UnifiedBookingBase):
    pass

class UnifiedBookingUpdate(UnifiedBookingBase):
    pass

class UnifiedBookingResponse(UnifiedBookingBase):
    id: int

    class Config:
        from_attributes = True


# --- Resource Schemas ---
class ResourceBase(BaseModel):
    resource_type: str
    resource_name: str
    default_availability: Optional[str]
    cost_per_unit: float
    cost_unit_type: str
    details: Optional[str]

class ResourceCreate(ResourceBase):
    pass

class ResourceUpdate(ResourceBase):
    pass

class ResourceResponse(ResourceBase):
    id: int

    class Config:
        from_attributes = True

# --- ResourceAvailability Schemas ---
class ResourceAvailabilityBase(BaseModel):
    resource_id: int
    date: date
    availability_type: str

class ResourceAvailabilityCreate(ResourceAvailabilityBase):
    pass

class ResourceAvailabilityResponse(ResourceAvailabilityBase):
    id: int

    class Config:
        from_attributes = True


# --- Policy Schemas ---
class PolicyBase(BaseModel):
    policy_type: str
    policy_text: str
    applies_to: str
    customer_visible: bool
    effective_date: date
    last_updated: Optional[date]
    admin_notes: Optional[str]

class PolicyCreate(PolicyBase):
    pass

class PolicyResponse(PolicyBase):
    id: int

    class Config:
        from_attributes = True


# --- Customer Schemas ---
class CustomerBase(BaseModel):
    name: str
    email: str
    phone: str
    address: Optional[str]

class CustomerCreate(CustomerBase):
    pass

class CustomerResponse(CustomerBase):
    id: int

    class Config:
        from_attributes = True


# --- Tour Schemas ---
class TourBase(BaseModel):
    name: str
    start_date: date
    end_date: date
    max_capacity: int
    current_bookings: Optional[int] = 0
    cost: float

class TourCreate(TourBase):
    pass

class TourResponse(TourBase):
    id: int

    class Config:
        from_attributes = True

# Base schema for Session
class SessionBase(BaseModel):
    date: date
    max_capacity: int
    current_bookings: Optional[int] = 0
    cost: float

# Schema for creating a new session
class SessionCreate(SessionBase):
    pass

# Schema for updating a session
class SessionUpdate(SessionBase):
    pass

# Schema for session responses
class SessionResponse(SessionBase):
    id: int

    class Config:
        from_attributes = True