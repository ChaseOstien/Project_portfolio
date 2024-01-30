from datetime import datetime
from db import Base
from sqlalchemy.orm import validates, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    project_id = Column(Integer, ForeignKey('projects.id'))
    created_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    user = relationship('User')

    @validates('comment_text')
    def validate_comment_text(self, key, comment_text):
        if not comment_text:
            raise AssertionError('No comment provided!')
        
        if len(comment_text) > 255:
            raise AssertionError('Comment must be less than 255 characters!')
        
        return comment_text
