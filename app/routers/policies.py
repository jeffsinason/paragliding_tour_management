from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.models.policy import Policy
from app.models.schemas import PolicyCreate, PolicyResponse

router = APIRouter(prefix="/policies", tags=["Policies"])

@router.get("/", response_model=list[PolicyResponse])
def get_policies(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    policies = db.query(Policy).offset(skip).limit(limit).all()
    return policies

@router.get("/{policy_id}", response_model=PolicyResponse)
def get_policy(policy_id: int, db: Session = Depends(get_db)):
    policy = db.query(Policy).filter(Policy.id == policy_id).first()
    if not policy:
        raise HTTPException(status_code=404, detail="Policy not found.")
    return policy

@router.post("/", response_model=PolicyResponse)
def create_policy(policy: PolicyCreate, db: Session = Depends(get_db)):
    new_policy = Policy(**policy.dict())
    db.add(new_policy)
    db.commit()
    db.refresh(new_policy)
    return new_policy

@router.put("/{policy_id}", response_model=PolicyResponse)
def update_policy(policy_id: int, policy: PolicyCreate, db: Session = Depends(get_db)):
    db_policy = db.query(Policy).filter(Policy.id == policy_id).first()
    if not db_policy:
        raise HTTPException(status_code=404, detail="Policy not found.")
    for key, value in policy.dict().items():
        setattr(db_policy, key, value)
    db.commit()
    db.refresh(db_policy)
    return db_policy

@router.delete("/{policy_id}")
def delete_policy(policy_id: int, db: Session = Depends(get_db)):
    policy = db.query(Policy).filter(Policy.id == policy_id).first()
    if not policy:
        raise HTTPException(status_code=404, detail="Policy not found.")
    db.delete(policy)
    db.commit()
    return {"message": "Policy deleted successfully."}