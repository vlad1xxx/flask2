from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/training/<prof>')
def index(prof):
    if 'инженер' in prof.lower() or 'строитель' in prof.lower():
        return render_template('training.html', station='нс')
    return render_template('training.html', station='ит')


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
