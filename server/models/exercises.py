from config import db
import ipdb

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)

class WorkoutPlan(db.Model):
    __tablename__ = 'workout_plans'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    routines = db.relationship('WorkoutRoutine', backref='plan')

class WorkoutRoutine(db.Model):
    __tablename__ = 'workout_routines'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    workout_plan_id = db.Column(db.Integer, db.ForeignKey('workout_plans.id'))
    repeat_interval = db.Column(db.Integer)
    routines = db.relationship('WorkoutRoutine', backref='plan')
    exercises = db.relationship('Exercise', backref='routine')


class Exercise(db.Model):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.Text)
    sets = db.Column(db.Integer)
    reps = db.Column(db.Integer)
    workout_routine_id = db.Column(db.Integer, db.ForeignKey('workout_routines.id'))

    def to_dict(self):
        return {'id': self.id, 'name': self.name}

    
