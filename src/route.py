from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

@app.route('/discussion-board')
def discussionBoard():
    return render_template('discussion-board.html')

@app.route('/lectures')
def lectures():
    return render_template('lectures.html')

@app.route('/tutorials')
def tutorials():
    return render_template('tutorials.html')

@app.route('/assignments')
def assignments():
    return render_template('assignments.html')

@app.route('/tests')
def tests():
    return render_template('tests.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)