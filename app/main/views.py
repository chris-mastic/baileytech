import secrets
from flask import Blueprint, render_template, request
import hmac
import subprocess

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
    
    return "OK", 200