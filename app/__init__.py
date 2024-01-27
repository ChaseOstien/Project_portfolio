from flask import Flask
from app.db import init_db

def create_app(test_config=None):
    app = Flask(__name__, static_url_path='/')
    app.url_map.strict_slashes = False
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    @app.route('/')
    def home():
        return 'Go to /hello'


    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    init_db(app)
    
    return app

