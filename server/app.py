from flask import make_response
from config import app

from models.exercises import Exercise

@app.route('/exercises', methods=['GET'])
def exercises():
    #finding all
    return make_response('all exercises shown here')