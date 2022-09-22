from flask import Flask, render_template, request
from faker import Faker
import requests

app = Flask(__name__)


@app.route('/requirements', methods=['get'])
def requirements():
    context = {}
    result = []

    with open('requirements.txt') as req_file:
        for line in req_file:
            line = line.rstrip('\n')
            result.append(line)
        context['result'] = result

    return render_template('requirements.html', **context)


@app.route('/generate-users', methods=['get', 'post'])
def generate_users():
    fake = Faker()
    context = {}

    if request.method == 'POST':
        result = []

        user_length = int(request.form['user_length'])
        for _ in range(user_length):
            result.append(f"{fake.name()}:{fake.email()}")
        context['result'] = result

    return render_template('generate_users.html', **context)


@app.route('/space', methods=['get'])
def space_mans():
    r = requests.get("http://api.open-notify.org/astros.json")
    space_mans_count = r.json()["number"]

    return f"Astronauts now: {space_mans_count}"


if __name__ == '__main__':
    app.run(debug=True)
