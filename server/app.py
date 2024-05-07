from flask import make_response
from config import app

@app.route('/exercises', methods=['GET'])
def exercises():
    #finding all
    return make_response('all exercises shown here')