from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

class CommentForm(FlaskForm):
    recaptcha = RecaptchaField()
    username = StringField(('Name'), validators=[DataRequired()])
    email = StringField(('Email'), validators=[DataRequired(), Email()])
    phone = StringField(('Phone'), validators=[DataRequired()])
    interest = StringField(('Interested In'), validators=[DataRequired()])
    submit = SubmitField('Contact Us')