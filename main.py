import random
from string import digits, ascii_letters, punctuation
from flask import Flask, render_template, request


app = Flask(__name__)
PWD_ALPHABET = f"{digits}{ascii_letters}{punctuation}"


@app.route('/', methods=['get'])
def index():
    return "Hello world!"


@app.route('/about', methods=['get'])
def about_us():
    return "This is about US!"


@app.route('/password_generator', methods=['get', 'post'])
def password_generator():
    context = {}

    if request.method == 'POST':
        pwd = ""
        pwd_length = int(request.form['pwd_length'])
        for _ in range(pwd_length):
            pwd += random.choice(PWD_ALPHABET)
        context['pwd'] = pwd

    return render_template('password_generator.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
