from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    """
    SQLAlchemy model for the 'users' table.
    Represents a user with an id, email, and hashed password.
    """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    posts = relationship("Post", back_populates="owner")

class Post(Base):
    """
    SQLAlchemy model for the 'posts' table.
    Represents a post with an id, text content, and owner_id.
    """
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="posts")
