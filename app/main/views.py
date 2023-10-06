import secrets
from flask import Blueprint, render_template, request
import hmac
import subprocess
import sh

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
def home():
    print(f"testing...another comment")
    return render_template('index.html')



@main.route('/update_server', methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = sh.git.Repo('https://github.com/chris-mastic/baileytech.git')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated Pythonanywhere successfully', 200
    else:
        return 'Wrong event type', 400
    
