from db import Base
from sqlalchemy import Column, Integer, ForeignKey

class Vote(Base):
    __tablename__ = 'votes'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    project_id = Column(Integer, ForeignKey('projects.id'))
