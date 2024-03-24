from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/distribution')
def index():
    people = ['участни1', 'участни2', 'участни3']
    return render_template('cabin.html', people=people)


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
