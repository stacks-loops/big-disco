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

@app.route('/exercises/<int:id>', methods=['GET'])
def exercise_by_id(id):
    found_exercise = Exercise.query.get(id)
    return make_response(found_exercise.to_dict())

@app.route('/exercises/<int:id>', methods=['PUT'])
def update_exercise(id):
    found_exercise = Exercise.query.get(id)
    if not found_exercise:
        return make_response({'error': 'Exercise not  found'}, 404)
    
    params = request.json
    found_exercise.name = params.get("name") #update only provided fields name

    db.session.commit()
    return make_response(found_exercise.to_dict(), 200)

@app.route('/exercises/<int:id>', methods=['DELETE'])
def delete_exercise(id):
    found_exercise = Exercise.query.get(id)
    if not found_exercise:
        return make_response({'error': 'Exercise not found'}, 404)
    
    db.session.delete(found_exercise)
    db.session.commit()
    return make_response({}, 204) #no content on delete success


