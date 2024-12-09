from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.models.resource_availability import ResourceAvailability
from app.models.schemas import ResourceAvailabilityCreate, ResourceAvailabilityResponse

router = APIRouter(prefix="/resource_availability", tags=["Resource Availability"])

@router.get("/", response_model=list[ResourceAvailabilityResponse])
def get_resource_availability(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    availability = db.query(ResourceAvailability).offset(skip).limit(limit).all()
    return availability

@router.get("/{availability_id}", response_model=ResourceAvailabilityResponse)
def get_single_availability(availability_id: int, db: Session = Depends(get_db)):
    availability = db.query(ResourceAvailability).filter(ResourceAvailability.id == availability_id).first()
    if not availability:
        raise HTTPException(status_code=404, detail="Availability not found.")
    return availability

@router.post("/", response_model=ResourceAvailabilityResponse)
def create_availability(availability: ResourceAvailabilityCreate, db: Session = Depends(get_db)):
    new_availability = ResourceAvailability(**availability.dict())
    db.add(new_availability)
    db.commit()
    db.refresh(new_availability)
    return new_availability

@router.put("/{availability_id}", response_model=ResourceAvailabilityResponse)
def update_availability(availability_id: int, availability: ResourceAvailabilityCreate, db: Session = Depends(get_db)):
    db_availability = db.query(ResourceAvailability).filter(ResourceAvailability.id == availability_id).first()
    if not db_availability:
        raise HTTPException(status_code=404, detail="Availability not found.")
    for key, value in availability.dict().items():
        setattr(db_availability, key, value)
    db.commit()
    db.refresh(db_availability)
    return db_availability

@router.delete("/{availability_id}")
def delete_availability(availability_id: int, db: Session = Depends(get_db)):
    availability = db.query(ResourceAvailability).filter(ResourceAvailability.id == availability_id).first()
    if not availability:
        raise HTTPException(status_code=404, detail="Availability not found.")
    db.delete(availability)
    db.commit()
    return {"message": "Availability deleted successfully."}