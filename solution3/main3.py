from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/auto_answer')
@app.route('/answer')
def index():
    human = {'title': 'Анкета', 'surname': 'Watny', 'name': 'Mark', 'education': 'выше среднего',
             'profession': 'марсоход', 'sex': 'male', 'motivation': 'Всегда мечтал застрять на Марсе', 'ready': 'True'}
    return render_template('auto_answer.html', human=human, title=human['title'])


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
