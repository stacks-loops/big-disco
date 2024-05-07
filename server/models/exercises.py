from config import db
import ipdb

daily_loop_exercises = db.Table(
    'daily_loop_exercises',
    db.Column('daily_loop_id', db.Integer, db.ForeignKey('daily_loop.id'), primary_key=True),
    db.Column('exercise_id', db.Integer, db.ForeignKey('exercises.id'), primary_key=True)
)

class DailyLoop(db.Model):
    __tablename__ = 'daily_loop'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    repeat_interval = db.Column(db.Integer)
    exercises = db.relationship(
        'Exercise',
        secondary=daily_loop_exercises,
        back_populates="daily_loops")

class Exercise(db.Model):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.Text)
    sets = db.Column(db.Integer)
    reps = db.Column(db.Integer)
    daily_loops = db.relationship(
        'DailyLoop',
        secondary=daily_loop_exercises,
        back_populates="exercises")

    def to_dict(self):
        return {
            'id': self.id, 
            'name': self.name,
            'description': self.description,
            'sets': self.sets,
            'reps': self.reps

        }

    
