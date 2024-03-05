import datetime
import json
import smtplib
from app import mail
from jinja2 import Template
from flask import Blueprint, render_template, flash, redirect, request, url_for
from flask_mail import Mail, Message
import git
import app
from app.form import CommentForm
from flask_mail import Message, Mail
from flask import Flask
import smtplib
import ssl
from email.mime.text import MIMEText



main = Blueprint('main', __name__, template_folder='templates')

# @main.route('/', methods=['GET'])
# def home():
#     print(f"testing...another test. Yay!!")
#     pub_key = "6LdJYR4pAAAAAOmQzWwtH5MHj0HCj8AXcaBsesgJ"
#     return render_template('index.html',pub_key=pub_key)

# @main.route('/validate', methods=['POST', 'GET'])
# def validate():
#     print('in validate view')
#     # if recaptcha.verify():
#     #     pass
#     # else:
#     #     pass
#     return json.dumps({"abc": True})

@main.route('/', methods = ['GET', 'POST'])
@main.route('/baileytech', methods = ['GET', 'POST'])
def comments():
    print("in comments")
    form = CommentForm()
    print(form.csrf_token)
    error = ''
    if form.is_submitted():
       
        if (request.form['g-recaptcha-response'] == ''):
            print(f"reacptcha value {request.form['g-recaptcha-response']}")
            print("not validate by recaptcha")
            error ='Please verify you are not a robot' 
            
            #return redirect(url_for('main.comments'))  
        else:
            #TODO: send email
            username = form.username.data
            email = form.email.data
            print(f"type of email {type(email)}")
            phone = form.phone.data
            interest = form.interest.data
            print(f"username {username}")
            print(f"email {email}")
            print(f"phone {phone}")
            print(f"interest {interest}")

            msg = MIMEText("Customer Enquiry.")
            msg["Subject"] = "Customer Engquiry"
            msg["From"] = "chrismazza@baileytech.tech"
            msg["To"] = "chrismazza@baileytech.tech"

            msg.set_payload(f"user {username} requested interest in {interest} and would like you to contact them at {phone} or {email} ")

            try:
                with smtplib.SMTP_SSL("smtp.zoho.com", 465) as server:
                    server.login("chrismazza@baileytech.tech", "iUN0BTF2CYmj")
                    server.send_message(msg)
                    print("Email sent successfully!")
            except Exception as e:
                print(f"Error sending email: {e}")

            #pass
    print({error})     
    return render_template('baileytech.html', title = 'Comment', error=error, form=form)