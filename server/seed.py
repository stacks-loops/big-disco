from config import app, db
from models.exercises import Exercise 

if __name__ == '__main__':
    with app.app_context():
        Exercise.query.delete()
        db.session.commit()

        squat = Exercise(name="squat")
        bench = Exercise(name="bench")
        deadlift = Exercise(name="deadlift")
        db.session.add_all([squat, bench, deadlift])
        db.session.commit()