from datetime import datetime
from app.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class Comment(Base):
  """
  Represents a comment made by a user on a post.

  Attributes:
    id (int): The primary key for the comment.
    comment_text (str): The text of the commend.
    user_id (int): The Id of the user who made the comment.
    post_id (int): The ID of the post the comment is associated with.
    created_at (datetime): The timestamp when the comment was created.
    updated_at (datetime): The timestamp when the comment was last updated.
  """
  __tablename__ = 'comments'
  
  id = Column(Integer, primary_key=True)
  comment_text = Column(String(255), nullable=False)
  user_id = Column(Integer, ForeignKey('users.id'))
  post_id = Column(Integer, ForeignKey('posts.id'))
  created_at = Column(DateTime, default=datetime.now)
  updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

  user = relationship('User')
