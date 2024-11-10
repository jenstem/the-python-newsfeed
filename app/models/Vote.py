from app.db import Base
from sqlalchemy import Column, Integer, ForeignKey

class Vote(Base):
  """
  Represents a vote in the voting system.

  Attributes:
    id (int): The unique identifier for the vote.
    user_id (int): The identifier of the user cast the vote.
    post_id (int): The identified of the post that received the vote.
  """
  __tablename__ = 'votes'
  id = Column(Integer, primary_key=True)
  user_id = Column(Integer, ForeignKey('users.id'))
  post_id = Column(Integer, ForeignKey('posts.id'))
