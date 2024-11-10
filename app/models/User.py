from app.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates
import bcrypt

salt = bcrypt.gensalt()

class User(Base):
  """
  Represents a user in the system with attributes for username, email, and password.
  """
  
  __tablename__ = 'users'
  
  id = Column(Integer, primary_key=True)
  username = Column(String(50), nullable=False)
  email = Column(String(50), nullable=False, unique=True)
  password = Column(String(100), nullable=False)

  @validates('email')
  def validate_email(self, key, email):
    """
    Validates that the email contains an '@' character.
    """
    assert '@' in email

    return email

  @validates('password')
  def validate_password(self, key, password):
    """
    Validates that the password is longer than four characters and encrypts it.
    """
    assert len(password) > 4

    return bcrypt.hashpw(password.encode('utf-8'), salt)

  def verify_password(self, password):
    """
    Verifies the provided password against the stored hashed password.
    """
    return bcrypt.checkpw(
      password.encode('utf-8'),
      self.password.encode('utf-8')
  )
