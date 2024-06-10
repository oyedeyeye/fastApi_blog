from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import schemas, dependencies
from app.database import get_db
from app.controllers import post_controller
from typing import List

# Define the router for post related routes
router = APIRouter(
    prefix="/posts",
    tags=["posts"]
)

@router.post("/addpost", response_model=schemas.Post)
def add_post(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: models.User = Depends(dependencies.get_current_user)):
    """
    Endpoint to add a new post.
    Requires text content and a valid user token for authentication.
    """
    return post_controller.add_post(db, post, current_user.id)

@router.get("/getposts", response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db), current_user: models.User = Depends(dependencies.get_current_user)):
    """
    Endpoint to get all posts of the current user.
    Requires a valid user token for authentication and implements caching.
    """
    return post_controller.get_posts(db, current_user.id)

@router.delete("/deletepost/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(dependencies.get_current_user)):
    """
    Endpoint to delete a post.
    Requires post ID and a valid user token for authentication.
    """
    return post_controller.delete_post(db, post_id, current_user.id)
