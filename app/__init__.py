from flask import Flask
from app.db import init_db
from flask_restful import Resource, Api
from app.api import projects

def create_app(test_config=None):
    app = Flask(__name__, static_url_path='/')
    app.url_map.strict_slashes = False
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    api = Api(app)
    
    init_db(app)

    app.register_blueprint(projects)
    
    return app
