import os
from flask import Flask, render_template
from flask_google_recaptcha import GoogleReCaptcha

basedir = os.path.abspath(os.path.dirname(__file__))

def create_app():
    app = Flask(__name__)
    recaptcha = GoogleReCaptcha(app=app)
    app.config.from_mapping(
        SECRET_KEY=os.getenv("FLASK_SECRET_KEY") or 'prc9FWjeLYh_KsPGm0vJcg',
        RECAPTCHA_SITE_KEY='6LdJYR4pAAAAAOmQzWwtH5MHj0HCj8AXcaBsesgJ',
        RECAPTCHA_SECRET_KEY='6LdJYR4pAAAAAFOaeMvNbjZpcJWPjyps5oiVBIuG',
        
    )
    
    
    from app.main.views import main
    
   
    app.register_blueprint(main)




    return app







