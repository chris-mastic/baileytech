import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY')
    RECAPTCHA_PRIVATE_KEY= os.environ.get('RECAPTCHA_PRIVATE_KEY')
    MAIL_SERVER='smtp.zoho.com'
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USERNAME='chrismazza@baileytech.tech'
    MAI_PASSWORD='pv6sC6Y!tL_Jxj4'
 
    

