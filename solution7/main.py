from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/table/<gender>/<int:age>')
def index(gender, age):
    if gender == 'male' and age >= 21:
        color = '#0000FF'
        img = '/static/img/adult.png'
    elif gender == 'male' and age < 21:
        color = '#42AAFF'
        img = '/static/img/child.png'
    elif gender == 'female' and age >= 21:
        color = '#FF0000'
        img = '/static/img/adult.png'
    elif gender == 'female' and age < 21:
        color = '#c76864'
        img = '/static/img/child.png'
    return render_template('colors.html', color=color, img=img)


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
