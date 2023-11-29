from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

class CommentForm(FlaskForm):
    username = StringField('Enter Name', validators=[DataRequired()])
    email = StringField('Enter Email', validators=[DataRequired(), Email()])
    phone = StringField('Enter Phone', validators=[DataRequired()])
    interest = StringField('Interested In', validators=[DataRequired()])
    submit = SubmitField('Post')