from config import app, db
from models.exercises import Exercise 

if __name__ == '__main__':
    with app.app_context():
        bench = Exercise(name="bench")
        deadlift = Exercise(name="deadlift")
        db.session.add_all([bench, deadlift])
        db.session.commit()