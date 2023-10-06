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



@main.route("/update", methods=["POST"])
def update():
    secret = '12345'
    # Verify the signature of the webhook request
    signature = request.headers.get("X-Hub-Signature")
    digest = hmac.new(secret, request.data, "sha1").hexdigest()
    if not hmac.compare_digest(signature, "sha1=" + digest):
        return "Invalid signature", 403
    
    # Pull the latest code from GitHub
    subprocess.run(["git", "pull", "origin", "main"])
    
    # Reload the web app
    subprocess.run(["touch", "/var/www/yourusername_pythonanywhere_com_wsgi.py"])

    @main.route('/update_server', methods=['POST'])
    def webhook():
        if request.method == 'POST':
            repo = git.Repo('https://github.com/chris-mastic/baileytech.git')
            origin = repo.remotes.origin
            origin.pull()
            return 'Updated Pythonanywhere successfully', 200
        else:
            return 'Wrong event type', 400
    

    
    return "OK", 200