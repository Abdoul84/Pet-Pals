from pet_pals.app import db, app

# Import your models
from pet_pals.models import Pet

# Create the database and tables
with app.app_context():
    db.drop_all()  # Optional: Drop all existing tables
    db.create_all()  # Create tables defined in your models
    print("Database initialized and tables created.")
