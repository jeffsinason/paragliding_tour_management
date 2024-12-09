from fastapi import FastAPI

# Importing the APIRouter class from the fastapi module
from app.routers import bookings, resources, resource_availability, policies, customers, tours, sessions

# Database Models and Schemas
from app.models.booking import UnifiedBooking
from app.models.resource import Resource
from app.models.resource_availability import ResourceAvailability
from app.models.policy import Policy
from app.models.customer import Customer
from app.models.tour import Tour
from app.models.session import Session

app = FastAPI()

# Including the routers in the main FastAPI app

app.include_router(bookings.router)
app.include_router(resources.router)
app.include_router(resource_availability.router)
app.include_router(policies.router)
app.include_router(customers.router)
app.include_router(tours.router)
app.include_router(sessions.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Paragliding Tour Management API"}
