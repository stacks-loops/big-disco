from config import db
import ipdb


class DailyLoop(db.Model):
    __tablename__ = 'daily_loop'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    repeat_interval = db.Column(db.Integer)

class Exercise(db.Model):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.Text)
    sets = db.Column(db.Integer)
    reps = db.Column(db.Integer)

    def to_dict(self):
        return {
            'id': self.id, 
            'name': self.name,
            'description': self.description,
            'sets': self.sets,
            'reps': self.reps

        }

    
