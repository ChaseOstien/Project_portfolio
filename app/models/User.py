from app.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates
from werkzeug.security import generate_password_hash, check_password_hash
import re

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)

    def set_password(self, password):
        if not password:
            raise AssertionError('No password provided!')
        
        if len(password) < 8 or len(password) > 20:
            raise AssertionError('Password must be between 8 and 20 characters!')

        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    @validates('username')
    def validate_username(self, username):
        if not username:
            raise AssertionError('No username provided!')
        
        if User.query.filter(User.username == username).first():
            raise AssertionError('Username already in use!')
        
        if len(username) < 5 or len(username) > 25:
            raise AssertionError('Username must be betweem 5 and 25 characters!')
        
        return username

    @validates('email')
    def validate_email(self, key, email):
        if not email:
            raise AssertionError('No email provided!')
        
        assert '@' in email

        return email


