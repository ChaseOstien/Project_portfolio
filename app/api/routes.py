from flask import Blueprint, jsonify
from flask_restful import Resource, Api
from app.models import User, Project, Comment, Vote
from app.db import get_db

projects = Blueprint('api', __name__)
api = Api(projects)

class Projects(Resource):
    def get(self):

        db = get_db()
        all_projects = db.query(Project).order_by(Project.id.asc()).all()

        projects_data = []
        for project in all_projects:
            project_data = {
                'id': project.id,
                'project_name': project.project_name,
                'project_description': project.project_description,
                'repo_link': project.repo_link,
                'deployed': project.deployed,
                'user_id': project.user_id,
                'created_at': project.created_at.isoformat(),  # Convert datetime to string
                'updated_at': project.updated_at.isoformat() if project.updated_at else None,
                # Include other properties as needed
            }
            projects_data.append(project_data)

        return jsonify(projects_data)
    
api.add_resource(Projects, '/hello')


