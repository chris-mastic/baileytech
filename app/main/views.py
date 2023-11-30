import datetime
import json
from app import app
from jinja2 import Template
from flask import Blueprint, render_template, flash, redirect, request, url_for
import git
from app.form import CommentForm


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
    if form.is_submitted():
        username = form.username.data
        email = form.email.data       
        print(f"reacptcha value {request.form['g-recaptcha-response']}")
        print('in form.validate')
        flash('Your comment is now live!')  
        return redirect(url_for('main.comments'))  
    print('s/b rendering template')
    
    return render_template('baileytech.html', title = 'Comment', form = form)