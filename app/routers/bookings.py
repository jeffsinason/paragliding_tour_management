from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.models.booking import UnifiedBooking
from app.models.schemas import UnifiedBookingCreate, UnifiedBookingResponse

router = APIRouter(prefix="/bookings", tags=["Bookings"])

#
# The read_bookings function is a GET request handler that returns a list of bookings from the database.
@router.get("/", response_model=list[UnifiedBookingResponse])
def read_bookings(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(UnifiedBooking).offset(skip).limit(limit).all()
#
# The create_booking function is a POST request handler that creates a new booking in the database.
@router.post("/", response_model=UnifiedBookingResponse)
def create_booking(booking: UnifiedBookingCreate, db: Session = Depends(get_db)):
    new_booking = UnifiedBooking(**booking.dict())
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return new_booking
#
# The get_booking function is a GET request handler that returns a single booking from the database.
@router.get("/{booking_id}", response_model=UnifiedBookingResponse)
def get_booking(booking_id: int, db: Session = Depends(get_db)):
    booking = db.query(UnifiedBooking).filter(UnifiedBooking.id == booking_id).first()
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking
#
# The update_booking function is a PUT request handler that updates a booking in the database.
@router.put("/{booking_id}", response_model=UnifiedBookingResponse)
def update_booking(booking_id: int, booking: UnifiedBookingCreate, db: Session = Depends(get_db)):
    db_booking = db.query(UnifiedBooking).filter(UnifiedBooking.id == booking_id).first()
    if not db_booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    
    # Update fields from the input schema
    for key, value in booking.dict().items():
        setattr(db_booking, key, value)
    
    db.commit()
    db.refresh(db_booking)
    return db_booking

@router.delete("/{booking_id}")
def delete_booking(booking_id: int, db: Session = Depends(get_db)):
    booking = db.query(UnifiedBooking).filter(UnifiedBooking.id == booking_id).first()
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    db.delete(booking)
    db.commit()
    return {"message": "Booking deleted successfully"}