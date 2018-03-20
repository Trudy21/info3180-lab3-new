from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
class MyForm(FlaskForm):
 name = StringField('Name', validators=[DataRequired()])
 email=StringField('Email Address' , validators=[DataRequired()])
 subject=StringField('Subject' , validators=[DataRequired()])
 message=StringField('Message' , validators=[DataRequired()])