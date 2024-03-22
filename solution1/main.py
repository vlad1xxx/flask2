from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/index/<name>')
def index(name):
    return render_template('base.html', title=name)


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
