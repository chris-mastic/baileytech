from flask import Blueprint, render_template, request
import git

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/', methods=['GET'])
def home():
    print(f"testing...another test. did this really work?")
    return render_template('index.html')


