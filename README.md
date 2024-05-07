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
pipenv install or pipenv --pyhton=3.8.13

install flask application (terminal)
pipenv install flask ipdb
** check Pipenv file to ensure creation

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
FLASK_APP=app.py
FLASK_RUN_PORT=5555 flask run
export FLASK_DEBUG=true
