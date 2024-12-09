from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.models.tour import Tour
from app.models.schemas import TourCreate, TourResponse

router = APIRouter(prefix="/tours", tags=["Tours"])

@router.get("/", response_model=list[TourResponse])
def get_tours(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    tours = db.query(Tour).offset(skip).limit(limit).all()
    return tours

@router.get("/{tour_id}", response_model=TourResponse)
def get_tour(tour_id: int, db: Session = Depends(get_db)):
    tour = db.query(Tour).filter(Tour.id == tour_id).first()
    if not tour:
        raise HTTPException(status_code=404, detail="Tour not found.")
    return tour

@router.post("/", response_model=TourResponse)
def create_tour(tour: TourCreate, db: Session = Depends(get_db)):
    new_tour = Tour(**tour.dict())
    db.add(new_tour)
    db.commit()
    db.refresh(new_tour)
    return new_tour

@router.put("/{tour_id}", response_model=TourResponse)
def update_tour(tour_id: int, tour: TourCreate, db: Session = Depends(get_db)):
    db_tour = db.query(Tour).filter(Tour.id == tour_id).first()
    if not db_tour:
        raise HTTPException(status_code=404, detail="Tour not found.")
    for key, value in tour.dict().items():
        setattr(db_tour, key, value)
    db.commit()
    db.refresh(db_tour)
    return db_tour

@router.delete("/{tour_id}")
def delete_tour(tour_id: int, db: Session = Depends(get_db)):
    tour = db.query(Tour).filter(Tour.id == tour_id).first()
    if not tour:
        raise HTTPException(status_code=404, detail="Tour not found.")
    db.delete(tour)
    db.commit()
    return {"message": "Tour deleted successfully."}