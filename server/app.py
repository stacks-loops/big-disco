from flask import make_response
from config import app

import ipdb

from models.exercises import Exercise

@app.route('/exercises', methods=['GET'])
def exercises():
    all_exercise_instances = Exercise.query.all()
    exercises_dict = [exercises.to_dict() for exercises in all_exercise_instances]

    return make_response(exercises_dict)