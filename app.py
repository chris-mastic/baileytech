from app import create_app
from flask_google_recaptcha import GoogleReCaptcha


app = create_app()
recaptcha = GoogleReCaptcha(app=app),

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, seed_db=seed_db)