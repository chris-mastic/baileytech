from flask import Blueprint, render_template, request
import git

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/', methods=['GET'])
def home():
    print(f"testing...another test. Yay!!")
    pub_key = "6LdJYR4pAAAAAOmQzWwtH5MHj0HCj8AXcaBsesgJ"
    return render_template('index.html',pub_key=pub_key)


