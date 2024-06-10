from sqlalchemy.orm import Session
from fastapi import HTTPException
from app import models, schemas, cache

def add_post(db: Session, post: schemas.PostCreate, user_id: int):
    """
    Handle the business logic for adding a new post.
    """
    db_post = models.Post(text=post.text, owner_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_posts(db: Session, user_id: int):
    """
    Handle the business logic for retrieving all posts of a user.
    """
    posts = cache.get_posts_cache(user_id)
    if posts is None:
        posts = db.query(models.Post).filter(models.Post.owner_id == user_id).all()
        cache.set_posts_cache(user_id, posts)
    return posts

def delete_post(db: Session, post_id: int, user_id: int):
    """
    Handle the business logic for deleting a post.
    """
    db_post = db.query(models.Post).filter(models.Post.id == post_id, models.Post.owner_id == user_id).first()
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    db.delete(db_post)
    db.commit()
    return {"detail": "Post deleted"}
