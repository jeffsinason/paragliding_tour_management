from fastapi import FastAPI

# Database Models and Schemas
from app.models.booking import UnifiedBooking
from app.models.resource import Resource, ResourceAvailability
from app.models.policy import Policy
from app.models.customer import Customer
from app.models.tour import Tour
from app.models.session import Session

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Paragliding Tour Management API"}
