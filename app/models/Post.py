from datetime import datetime
from app.db import Base
from .Vote import Vote
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, select, func
from sqlalchemy.orm import relationship, column_property


class Post(Base):
  """
  Represents a blog post in the database.

  Attributes:
    id (int): Unique identifier for the post.
    title (str): Title of the post.
    post_url (str): URL slug for the post.
    user_id (int): Foreign key linking to the User model.
    created_at (datetime): Timestamp of when the post was created.
    updated_at (datetime): Timestamp of when the post was last updated.
    vote_count (int): Count of votes associated with the post.
  """
  
  __tablename__ = 'posts'
  
  id = Column(Integer, primary_key=True)
  title = Column(String(100), nullable=False)
  post_url = Column(String(100), nullable=False)
  user_id = Column(Integer, ForeignKey('users.id'))
  created_at = Column(DateTime, default=datetime.now)
  updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
  vote_count = column_property(
  select(func.count(Vote.id)).where(Vote.post_id == id)
)

  user = relationship('User')
  comments = relationship('Comment', cascade='all,delete')
  votes = relationship('Vote', cascade='all,delete')
