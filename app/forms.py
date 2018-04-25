from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField
from wtforms.validators import DataRequired, Email


class MyForm(FlaskForm):
    name = StringField('Name (Required)', validators=[DataRequired()])
    email = StringField('Email (Required)', validators=[DataRequired(), Email()])
    subject=StringField('Subject (Required)', validators=[DataRequired()])
    message=StringField('Message (Required)', validators=[DataRequired()])