from flask import Flask, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from scrapers.codechef import CodeChef
from scrapers.codeforces import CodeForces

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# app.config['SQLALCHEMY_BINDS'] = {
#     'students' : 'sqlite:///students.db',
#     'professors' : 'sqlite:///professors.db'
# }

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<User %r>' %self.id

@app.route('/')
def index():

    if 'username' in session:
        return redirect('/dashboard')

    # return render_template('index.html')
    return render_template('/index.html')

@app.route('/dashboard')
def dashboard():

    if 'username' not in session:
        return render_template('/login.html',Message="You have to login!")

    ccContests = CodeChef().getFutureContests()
    cfContests = CodeForces().getFutureContests()
    ccNoC = len(ccContests["Name"])
    cfNoC = len(cfContests["Name"])
    return render_template('dashboard.html',username = session['username'],ccNoC = ccNoC, ccContests = ccContests, cfNoC = cfNoC, cfContests = cfContests)

@app.route('/login', methods=['POST', 'GET'])
def login():

    if request.method == 'POST':
        user_name = request.form['username']
        pass_word = request.form['password']

        try:
            
            result = Users.query.filter_by(username=user_name, password=pass_word).first()

            if result is None:
                return render_template('/login.html',Message="Wrong Credentials")

            else:
                session['username'] = user_name
                return redirect('/dashboard')

        except:
            return render_template('/login.html',Message="Wrong Credentials")
    
    else:
        return render_template('login.html')

@app.route('/signup', methods=['POST', 'GET'])
def signup():

    if request.method == 'POST':
        user_name = request.form['username']
        pass_word = request.form['password']

        new_user = Users(
            username = user_name,
            password = pass_word,
            )

        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect('/login')
        except:
            return redirect('/error')
    
    else:
        return render_template('signup.html')

@app.route('/signout')
def signout():
    session.pop('username', None)
    return redirect('/login')

if __name__ == '__main__':
    # db.create_all()
    app.run(debug=True)