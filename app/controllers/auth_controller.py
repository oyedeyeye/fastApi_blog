from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app import models, dependencies, schemas

def signup(db: Session, user: schemas.UserCreate):
    """
    Handle the business logic for user signup.
    """
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = dependencies.get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def login(db: Session, user: schemas.UserLogin):
    """
    Handle the business logic for user login.
    """
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if not db_user or not dependencies.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token = dependencies.create_access_token(data={"sub": str(db_user.id)})
    return {"access_token": access_token, "token_type": "bearer"}
