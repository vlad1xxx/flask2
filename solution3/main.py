from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/list_prof/<list>')
def index(list):
    if list in ['ol', 'ul']:
        prof = ['инженер', 'пилот', ' строитель', 'врач', 'штурман']
        return render_template('base.html', prof=prof, type=list)
    else:
        return '<p1>Ошибка. Используйте ol или ul</p1>'


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
