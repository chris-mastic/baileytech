from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email

class CommentForm(FlaskForm):
    recaptcha = RecaptchaField()
    username = StringField(('Name'), validators=[DataRequired()])
    email = StringField(('Email'), validators=[DataRequired(), Email()])
    phone = StringField(('Phone'), validators=[DataRequired()])
    service_interest = [('placeholder', 'Please select a service you are interested in ...'),('website', 'Website'), ('support', 'Support'), ('software', 'Software'), ('automation', 'Automation')]
    interest = SelectField(('Interested In'), validators=[DataRequired()],choices=service_interest, default='placeholder')
    submit = SubmitField('Contact Us')