from config import db
import ipdb

class Exercise(db.Model):
    __tablename__ = 'Exercises'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    
