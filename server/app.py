from flask import make_response
from config import app

import ipdb

from models.exercises import Exercise

@app.route('/exercises', methods=['GET'])
def exercises():
    ipdb.set_trace()
    return make_response('all exercises shown here')