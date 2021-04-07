from flask import Flask, render_template, url_for, g, request, session, redirect
from functools import wraps
from flask_session import Session
import os
import sqlite3

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = 'super secret key'
Session(app)

DATABASE = "./assignment3.db"

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

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('username') is None:
            return redirect('/', code=302)
        return f(*args, **kwargs)
    return decorated_function

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def loginpage():
    return render_template('login.html')

@app.route("/home")
def home():
    return render_template('index.html')

@app.route('/login', methods= ['POST'])
def login():
    # extract username and password from the request
    username = request.form['username']
    password = request.form['password']
    user = query_db('select * from user where username = ?', [username], one=True)
    if user is None:
        print("user is none")
        return render_template("login-result.html", user_exist=False)
    else:
        pw = user[1]
        role = user[2]
        if password == pw:
            session['username'] = username
            session['role'] = role
            # keeping the if in case you want to add something. otherwise no need for if else.
            if role == 'student':
                return index()
            else:
                return index()
        else:
            return render_template("login-result.html", user_exist=True, password_correct=False)

@app.route('/logout')
def logout():
    session['username'] = None
    session['role'] = None
    return redirect('/', code=302)

@app.route("/signup")
def signup():
    return render_template('account.html')

@app.route('/account', methods = ['POST'])
def account():
    username = request.form['username']
    password = request.form['password']
    role = request.form['role']
    try:
        db = get_db()
        cur = db.execute(
            'INSERT INTO user (username, password, role) values (?,?,?)',
            (
                username,
                password,
                role
            )
        )
        db.commit()
        return render_template('account-result.html', account_created=True)
    except:
        return render_template('account-result.html', account_created=False)

@app.route("/index")
def index():
    return render_template('index.html', name=session.get('username', 'not set'))

@app.route('/student')
@login_required
def student(username):
    return render_template('student.html')

@app.route('/instructor')
@login_required
def instructor(username):
    return render_template('instructor.html')

@app.route('/calendar')
@login_required
def calendar():
    return render_template('calendar.html', name=session.get('username', 'not set'))

@app.route('/discussion-board')
@login_required
def discussionBoard():
    return render_template('discussion-board.html', name=session.get('username', 'not set'))

@app.route('/lectures')
@login_required
def lectures():
    return render_template('lectures.html', name=session.get('username', 'not set'))

@app.route('/tutorials')
@login_required
def tutorials():
    return render_template('tutorials.html', name=session.get('username', 'not set'))

@app.route('/assignments')
@login_required
def assignments():
    return render_template('assignments.html', name=session.get('username', 'not set'))

@app.route('/tests')
@login_required
def tests():
    return render_template('tests.html', name=session.get('username', 'not set'))

@app.route('/resources')
@login_required
def resources():
    return render_template('resources.html', name=session.get('username', 'not set'))

# Helper function for /feedback: Returns all instructors in the DATABASE
def getInstructors():
    #connect to the database
    db = get_db()
    db.row_factory = make_dicts

    #creating cursor and select distinct from user table
    cur = db.cursor()
    cur.execute("select distinct username from user where role= ?", ['instructor'])
    
    rows = cur.fetchall()
    #close connection
    cur.close()
    return rows

# Helper function for /feedback: Returns all feedback to (instructor) in the DATABASE
def get_feedback(name):
    #connect to the database
    db = get_db()
    db.row_factory = make_dicts

    cur = db.cursor()
    cur.execute("select * from feedback where feedback_to= ?", [name])
    
    rows = cur.fetchall()
    #close connection
    cur.close()
    return rows

@app.route('/feedback')
@login_required
def feedback():
    if session.get('role', 'not set') == 'student':
        rows = getInstructors()
        return render_template('student-feedback.html', rows = rows, name=session.get('username', 'not set'))

    elif session.get('role', 'not set') == 'instructor':
        feedbacks = get_feedback(session.get('username', 'not set'))
        return render_template('instructor-feedback.html', feedbacks = feedbacks, name=session.get('username', 'not set'))

    else:
        return "Session not set"

@app.route('/feedback-submitted', methods= ['POST', 'GET'])
@login_required
def feedbackSubmitted():
    if request.method == 'POST':
        try:
            # getting the post body
            inst = request.form['instructor']
            qa = request.form['feedback-qa']
            qb = request.form['feedback-qb']
            qc = request.form['feedback-qc']
            qd = request.form['feedback-qd']

            # connect to DATABASE and make a cursor from it
            db = get_db()
            #insert into table
            cur = db.execute(
                "INSERT INTO feedback(feedback_to,date_time,question_a,question_b,question_c,question_d) values (?,datetime('now'),?,?,?,?)",
                (inst,qa,qb,qc,qd) 
            )
            
            db.commit()
            # close the cursor
            cur.close()
            # ensuring commitment suceed
            msg = "Feedback has been recieved. Thank your for your feedback!"
        except:
            msg = "There is an error in insert operation. Please fill it in again."

        finally:
            return render_template('feedback-submitted.html', msg = msg, name=session.get('username', 'not set'))
    # render template if it is GET
    return render_template('feedback-submitted.html', name=session.get('username', 'not set'))


def get_grades(types):
    # connect to database
    db=get_db()
    db.row_factory = make_dicts

    # get students
    students = []
    for student in query_db('SELECT DISTINCT username FROM grade ORDER BY username'):
        students.append(student['username'])

    # initialze a list of dictionaries based on students and types
    grades = []
    for student in students:
        tmp = {}
        tmp['username'] = student
        for grade in query_db('SELECT type, grade FROM grade WHERE username = ?', [student]):
            tmp[grade['type']] = grade['grade']
        grades.append(tmp)

    # fill up unavaliable grades
    for grade in grades:
        for t in types:
            if t not in grade.keys():
                grade[t] = 'N/A'
    return grades

def get_remarks():
    # connect to database
    db=get_db()
    db.row_factory = make_dicts

    # get remarks
    remarks = []
    for remark in query_db('SELECT * FROM remark ORDER BY date_time DESC'):
        remarks.append(remark)

    return remarks

# Helper function for /grade: Return the grades of current user student with a list of subject (types)
def getMyGrades(types):
    #Student side
    #connect to the database
    db = get_db()
    db.row_factory = make_dicts

    # getting the post body
    username=session.get('username', 'not set')
    cur = db.cursor()
    cur.execute("select * from grade where username= ?", [username])
    
    rows = cur.fetchall()

    #making empty 'type' are shown as 'grade': 0 
    exist = False
    temp = {}
    for t in types:
        for r in rows:
            if r['type'] == t: exist = True
        if not exist:
            temp = {'username' : username, 'type': t, 'date_time': 'N/A', 'grade': 0}
            rows.append(temp)
        exist=False

    # close the cursor
    cur.close()
    return rows

# Helper function for /grade: Return the remark request type and its status
def getMyRemarkRequest():
    #connect to the database
    db = get_db()
    db.row_factory = make_dicts
    name=session.get('username', 'not set')
    
    #creating cursor and select from remark table
    cur = db.cursor()
    cur.execute("select type, status from remark where username= ?", [name])
    
    remarkRequests = cur.fetchall()
    #close connection
    cur.close()
    return remarkRequests

@app.route('/grades')
@login_required
def grades():
    types = ["A1", "A2", "A3","Labs", "TT1", "TT2", "Final"]
    
    if session.get('role', 'not set') == 'student':
        rows = getMyGrades(types)
        remarkRequests = getMyRemarkRequest()

        return render_template('my-grade.html', rows = rows, remarkRequests = remarkRequests, username=session.get('username', 'not set'))

    elif session.get('role', 'not set') == 'instructor':

        grades = get_grades(types)
        remarks = get_remarks()

        return render_template('grades-instructor.html', name=session.get('username', 'not set'),  types=types, grades=grades, remarks=remarks)
    else:
        return "Session not set"

@login_required
def updateGrade():
    # extract new grade from the request
    name = request.form['name']
    t = request.form['type']
    oldGrade = request.form['oldGrade']
    newGrade = request.form['newGrade']

    if oldGrade == "N/A":
        try:
            db = get_db()
            cur = db.execute(
                "INSERT INTO grade values (?, ?, datetime('now'), ?)",
                (
                    name,
                    t,
                    newGrade
                )
            )
            db.commit()
        except:
            return "error"
    else:
        try:
            db = get_db()
            cur = db.execute(
                "UPDATE grade SET grade = ? WHERE username = ? AND type = ?",
                (
                    newGrade,
                    name,
                    t
                )
            )
            db.commit()
        except:
            return "error"
    return grades()

def updateRemark(status):
    # extract form information from the request
    name = request.form['name']
    date_time = request.form['date-time']

    # Try to update the status of the remark
    try:
        db = get_db()
        cur = db.execute(
            "UPDATE remark SET status = ? WHERE username = ? AND date_time = ?",
            (
                status,
                name,
                date_time
            )
        )
        db.commit()
    except:
        return "error"

    # render the grades page again
    return grades()

@app.route('/grades', methods= ['POST'])
@login_required
def update():
    # there are three possible actions in the grades page
    # call the corresponding function based on actions
    action = request.form['action']
    if action == 'editGrade':
        return updateGrade()
    elif action == "startRemarking":
        return updateRemark('In progress')
    elif action == "doneRemarking":
        return updateRemark('Addressed')

@app.route('/remark-request-submitted', methods= ['POST', 'GET'])
@login_required
def remarkRequestSubmitted():
    if request.method == 'POST':
        try:
            # getting the post body
            markType = request.form['mark-type']
            requestText = request.form['remark-request']
            username=session.get('username', 'not set')

            # connect to DATABASE and make a cursor from it
            db = get_db()

            curRequests = getMyRemarkRequest()
            existR = False
            for curRequest in curRequests:
                print(curRequest['type'])
                if curRequest['type'] == markType:
                    existR = True
            
            if existR:
                #update table as it is already existed
                cur = db.execute(
                    
                    "UPDATE remark SET status = ?, request = ? WHERE username = ? AND type = ?",
                    (
                        'Not yet started',
                        requestText,
                        username, 
                        markType
                    ) 
                )
            elif not existR:
                #insert into table
                cur = db.execute(
                    "INSERT INTO remark(username,type,date_time,request,status) VALUES (?,?,datetime('now'),?,'Not yet started')",
                    (username,markType,requestText) 
                )

            db.commit()

            # close the cursor
            cur.close()
            # ensuring commitment suceed
            msg = ("Remark Request for " + markType + " has been recieved. Please be patient")
        except:
            msg = "Something went wrong in requesting remark. Please fill it in again."

        finally:
            return render_template('remark-submitted.html', msg = msg, name=session.get('username', 'not set'))
    # render template if it is GET
    return render_template('remark-submitted.html', name=session.get('username', 'not set'))

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
