import smtplib
from jinja2 import Template
from flask import Blueprint, render_template, flash, redirect, request, url_for, flash
from app.form import CommentForm
import smtplib
from email.mime.text import MIMEText



main = Blueprint('main', __name__, template_folder='templates')

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
                    flash("Message sent. Thank you!!", "success")
            except Exception as e:
                print(f"Error sending email: {e}")

            #pass
    print({error})     
    return render_template('baileytech.html', title = 'Comment', error=error, form=form)