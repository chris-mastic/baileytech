from flask_mail import Message, Mail
from flask import Flask
import smtplib
import ssl
from email.mime.text import MIMEText

app = Flask(__name__)

#----------------------------------------------------WORKS FOR ZOHO - FINALLY

msg = MIMEText("Hello, this is a test email.")
msg["Subject"] = "Test Email"
msg["From"] = "chrismazza@baileytech.tech"
msg["To"] = "chrismazza@baileytech.tech"

try:
    with smtplib.SMTP_SSL("smtp.zoho.com", 465) as server:
        server.login("chrismazza@baileytech.tech", "iUN0BTF2CYmj")
        server.send_message(msg)
        print("Email sent successfully!")
except Exception as e:
    print(f"Error sending email: {e}")
# ------------------------------------------------WORKS FOR GMAIL
# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USE_SSL'] = True
# app.config['MAIL_USERNAME'] = 'clmaz031882@gmail.com'
# app.config['MAIL_PASSWORD'] = 'kqrc aegj wpdj mner'


# mail = Mail(app)

# msg = MIMEText("Hello, this is a test email.")
# msg["Subject"] = "Test Email"
# msg["From"] = "chritopher.mazza@orleansassessors.com"
# msg["To"] = "clmaz031882@gmail.com"


# try:
#     with smtplib.SMTP("smtp.gmail.com", 587) as server:
#             server.starttls()
#             server.login("clmaz031882@gmail.com", "kqrc aegj wpdj mner")
#             server.send_message(msg)
#             print("Email sent successfully!")
# except Exception as e:
#     print(f"Error sending email: {e}")


