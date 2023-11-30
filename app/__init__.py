import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from config import Config


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config.from_object(Config)

print(f"app.config {app.config}")
print(f"env vars private {os.environ.get('RECAPTCHA_PRIVATE_KEY')}")
print(f"env vars public {os.environ.get('RECAPTCHA_PUBLIC_KEY')}")
print(f"env vars secret {os.environ.get('SECRET_KEY')}")

bootstrap = Bootstrap(app)
moment = Moment(app)

from app.main.views import main
app.register_blueprint(main)

# def create_app():
#     app = Flask(__name__)
    
#     app.config.from_mapping(
#         SECRET_KEY=os.getenv("FLASK_SECRET_KEY") or 'prc9FWjeLYh_KsPGm0vJcg',
#         RECAPTCHA_SITE_KEY='6LdJYR4pAAAAAOmQzWwtH5MHj0HCj8AXcaBsesgJ',
#         RECAPTCHA_PRIVATE_KEY='6LdJYR4pAAAAAFOaeMvNbjZpcJWPjyps5oiVBIuG',
        
#     )
    
    
#     from app.main.views import main
    
   
#     app.register_blueprint(main)




#     return app







