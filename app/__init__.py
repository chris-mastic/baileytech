import os
from flask import Flask, render_template

basedir = os.path.abspath(os.path.dirname(__file__))


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.getenv("FLASK_SECRET_KEY") or 'prc9FWjeLYh_KsPGm0vJcg',
    )

    from app.main.views import main
    
   
    app.register_blueprint(main)




    return app







