from app.db import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, select, func
from sqlalchemy.orm import validates, relationship, column_property
from datetime import datetime
from .Vote import Vote

class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    project_name = Column(String(50), nullable=False)
    project_description = Column(String(100), nullable=False)
    repo_link = Column(String(100), nullable=False)
    deployed = Column(String(100), nullable=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    user = relationship('User')
    comments = relationship('Comment', cascade='all, delete')
    votes = relationship('Vote', cascade='all,delete')
    vote_count = column_property(
        select(func.count(Vote.id)).where(Vote.project_id == id).scalar_subquery()
    )


    @validates('project_name')
    def validate_project_name(self, project_name):
        if not project_name:
            raise AssertionError('No project name provided!')
        
        if len(project_name) < 3 or len(project_name) > 25:
            raise AssertionError('Project name must be betweem 3 and 25 characters!')
        
        return project_name
    
    @validates('project_description')
    def validate_project_description(self, project_description):
        if not project_description:
            raise AssertionError('No project description provided!')
        
        if len(project_description) > 100:
            raise AssertionError('Your project description must be less than 100 characters!')
        
        return project_description

