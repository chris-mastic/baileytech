import json
from flask import Blueprint, render_template, request
from flask_google_recaptcha import GoogleReCaptcha
import git


main = Blueprint('main', __name__, template_folder='templates')

@main.route('/', methods=['GET'])
def home():
    print(f"testing...another test. Yay!!")
    pub_key = "6LdJYR4pAAAAAOmQzWwtH5MHj0HCj8AXcaBsesgJ"
    return render_template('index.html',pub_key=pub_key)

@main.route('/validate', methods=['POST', 'GET'])
def validate():
    print('in validate view')
    # if recaptcha.verify():
    #     pass
    # else:
    #     pass
    return json.dumps({"abc": True})