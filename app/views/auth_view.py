from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import schemas, dependencies
from app.database import get_db
from app.controllers import auth_controller

# Define the router for authentication related routes
router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/signup", response_model=schemas.UserCreate)
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    Endpoint for user signup.
    Accepts email and password, and creates a new user.
    """
    return auth_controller.signup(db, user)

@router.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    """
    Endpoint for user login.
    Accepts email and password, and returns a JWT token if successful.
    """
    return auth_controller.login(db, user)
