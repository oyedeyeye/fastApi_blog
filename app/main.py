from fastapi import FastAPI
from app.views import auth_view, post_view
from app.database import engine, Base

# Create all database tables
Base.metadata.create_all(bind=engine)

# Initialize FastApi app
app = FastAPI()

# Include routers for different endpoints
app.include_router(auth_view.router)
app.include_router(post_view.router)
