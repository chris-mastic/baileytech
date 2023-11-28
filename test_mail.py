from flask_mail import Mail, Message
from flask import Flask

app = Flask(__name__)

EMAIL_USE_TSL = True
EMAIL_HOST = 'smtp.zoho.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'chrismazza@baileytech.tech'
EMAIL_HOST_PASSWORD = 'baileyTech#23'
DEFAULT_FROM_EMAIL = 'chrismazza@baileytech.tech'
SERVER_EMAIL = 'chrismazza@baileytech.tech'

mail = Mail(app)

msg = Message('Hello', sender = 'christopher.mazza@orleansassessors.com', recipients = ['chrismazza@baileytech.tech'])
msg.body = "Hello Flask message sent from Flask-Mail"
mail.send(msg)
