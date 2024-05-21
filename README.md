just getting things started

# Terminal Environment Changes

## Extension: vscode.git

Enables the following features: git auth provider

- `GIT_ASKPASS=/Applications/Visual Studio Code.app/Contents/Resources/app/extensions/git/dist/askpass.sh`
- `VSCODE_GIT_ASKPASS_NODE=/Applications/Visual Studio Code.app/Contents/Frameworks/Code Helper (Plugin).app/Contents/MacOS/Code Helper (Plugin)`
- `VSCODE_GIT_ASKPASS_EXTRA_ARGS=`
- `VSCODE_GIT_ASKPASS_MAIN=/Applications/Visual Studio Code.app/Contents/Resources/app/extensions/git/dist/askpass-main.js`
- `VSCODE_GIT_IPC_HANDLE=/var/folders/dh/xwf4p4qd60lg5vymvry_4h2w0000gn/T/vscode-git-af28874f9c.sock`

## Extension: ms-python.python

- `PATH=/Users/parkerconnolly/.vscode/extensions/ms-python.python-2024.4.1/python_files/deactivate/zsh:/Users/parkerconnolly/Development/code/phase-6/big-disco/.venv/bin:${env:PATH}`
- `VIRTUAL_ENV=/Users/parkerconnolly/Development/code/phase-6/big-disco/.venv`
- `VIRTUAL_ENV_PROMPT=big-disco`
- `PS1=big-disco${env:PS1}`


FRONTEND
cd frontend    
npm start


BACKEND

Creating a backend with flask SQLAlchemy

Create virtual environment (terminal)
pipenv install or pipenv --python=3.8.13

install flask application (terminal)
pipenv install flask ipdb
** check Pipenv file to ensure creation

Open shell
pipenv shell

Check flask is working (commands will not run yet)
flask

Make server directory
mkdir server
cd server

Create app.py and config file(terminal)
touch app.py config.py

Import Flask class to config.py
from flask import Flask

Create a Flask instance to configure the flask application (config.py)
app = Flask(__name__)

Import into app.py (app.py)
from config import app

Declare where the app is configured (terminal)
FLASK_APP=app.py

Set run port and run the server (terminal)
FLASK_RUN_PORT=5555 flask run

Turn debug on (terminal) - this restarts the server when we change app.py so we don't have to manually
use ctrl + C to kill the server then:
export FLASK_DEBUG=true

Start the server back up
ANYTIME YOU EXIT THE VIRTUAL ENVIRONMENT, MUST SET ENVIRONMENT VARIABLES AGAIN
cd server

FLASK_APP=app.py
export FLASK_DEBUG=true
FLASK_RUN_PORT=5555 flask run

Create a basic test route (app.py)
from flask import make_response
from config import app

@app.route('/exercises', methods=['GET'])
def exercises():
    #finding all
    return make_response('all exercises shown here')

Go to Postman and make a get request to http://localhost:5555/exercises

GOOD JOB!!

Let's get into Flask SQLAlchemy library that will give us access to those methods
This way our classes can inherit methods
Press ctrl C
In virtual enviornment in server
pipenv install flask-sqlalchemy

Create a new SQLAlchemy instance (config.py)
Added
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy

New
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aardvark.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()

Any datbase can be used i.e. Postgres

Install migrate library(terminal)
pipenv install flask-migrate

Check flask to ensure db is available
use flask shell to test within your application

CREATE A CLASS

New folder models
New file exercises.py

Here is exercises.py
from config import db
import ipdb

# class Exercises(db.Model):
#     pass

class Test:
    def goofin(self):
        print('goofin off')

class Activity(Test):
    __tablename__ = 'Activities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)

ipdb.set_trace()

When we want to create a new migration repository we use the init command in db

Delete the ipdb line in exercises.py server in terminal 
flask db init

This should create an instance and migrations folder

Now we use the migrate command to generate a revision file. When we make changes to models
that are used by app.py make a commit sort of. In virtual env and in server.
Delete the testing code and use this in exercises.py
--
from config import db
import ipdb

class Exercise(db.Model):
    __tablename__ = 'Exercises'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    
--
then... this is all done JUST IN SERVER NO SHELL OR ANYTHING

flask db migrate -m "create Activity table"

Can view the db by right clicking > "Open With" SQLite Explor OR SQLite Viewer

update the database(terminal)
flask db upgrade

Create seed.py file in the server folder

seed.py
from config import app, db
from models.exercises import Exercise 

if __name__ == '__main__':
    with app.app_context():
        Exercise.query.delete()
        db.session.commit()

        bench = Exercise(name="bench")
        deadlift = Exercise(name="deadlift")
        db.session.add_all([bench, deadlift])
        db.session.commit()

Run the file using python (in server directory in terminal)
python seed.py



Update app.py with this code to retrieve a dictionary of exercises
from flask import make_response, request
from config import app, db

import ipdb

from models.exercises import Exercise

@app.route('/exercises', methods=['GET', 'POST'])
def exercises():
    if request.method == 'GET':
        all_exercise_instances = Exercise.query.all()
        exercises_dict = [exercises.to_dict() for exercises in all_exercise_instances]

        return make_response(exercises_dict)

    elif request.method == 'POST':
        params = request.json
        new_exercise = Exercise(name=params["name"])

        db.session.add(new_exercise)
        db.session.commit()
        return make_response(new_exercise.to_dict(), 201)

In exercises.py add this to create the to_dict method so we do not have to input every time.
This goes under the name column creation line

def to_dict(self):
        return {'id': self.id, 'name': self.name}

Open Postman again and change to POST request (which is to add not retreive)
Input our endpoint http://localhost:5555/exercises
Press headers below the input bar and add Content-Type in "Key" column and "application/json" in value
To the right of headers select "Body"
Change to "raw" and ensure the far right dropdown is set to JSON in blue
Input this into text box
{
    "name" : "pullup"
}

Press SEND!

MIGRATION ISSUES
delete aardvark.db and migrations folder
in server in terminal
flask db init
flask db migrate -m "some name"
flask db upgrade




