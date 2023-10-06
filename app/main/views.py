import secrets
from flask import Blueprint, render_template, request
import hmac
import subprocess
import git

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
def home():
    print(f"testing... I hope this works. Now I added a secret. We will see...Failed. Maybe now")
    return render_template('index.html')



@main.route('/update_server', methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('https://github.com/chris-mastic/baileytech.git')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated Pythonanywhere successfully', 200
    else:
        return 'Wrong event type', 400
    
