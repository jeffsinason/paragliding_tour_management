from app.database.db import Base, engine
# Database Models and Schemas
from app.models.booking import UnifiedBooking
from app.models.resource import Resource, ResourceAvailability
from app.models.policy import Policy
from app.models.customer import Customer
from app.models.tour import Tour
from app.models.session import Session
# Import additional models as needed

# Create all tables
print("Creating database tables...")
Base.metadata.create_all(bind=engine)
print("Tables created successfully!")