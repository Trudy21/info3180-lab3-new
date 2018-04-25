from flask import Flask
from flask_mail import Mail

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Hello Trudy'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '2525'
app.config['MAIL_USERNAME'] = '8341eaded311e2'
app.config['MAIL_PASSWORD'] = 'f77309ddaaccc4'
mail = Mail(app)

from app import views

