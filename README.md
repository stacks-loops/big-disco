just getting things started


FRONTEND
cd frontend    
npm start

BACKEND

Creating a backend with flask SQLAlchemy
Create virtual environment
pipenv install or pipenv --pyhton=3.8.13

install flask application
pipenv install flask ipdb
** check Pipenv to ensure creation

Create app.py and config file
touch app.py config.py

Import Flask class to config.py
from flask import Flask

Create a Flask instance to configure the flask application
app = Flask(__name__)

Import into app.py
from config import app