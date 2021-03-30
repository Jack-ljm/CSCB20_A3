from flask import Flask, render_template, url_for, g
import os
import sqlite3

app = Flask(__name__)

DATABASE = "./A3.db"

# The following three functions are taken from here
# https://flask.palletsprojects.com/en/1.1.x/patterns/sqlite3/
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.ddl', mode='r') as f:
            db.cursor().executescript(f.read())
        with app.open_resource('dummyData.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

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

init_db()