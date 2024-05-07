from config import app, db
from models.exercises import DailyLoop, Exercise

if __name__ == '__main__':
    with app.app_context():
        Exercise.query.delete()
        DailyLoop.query.delete()
        db.session.commit()

        push_routine = DailyLoop(name='Push', repeat_interval=3)
        pull_routine = DailyLoop(name='Pull', repeat_interval=3)
        leg_routine = DailyLoop(name='Legs', repeat_interval=3) 
        db.session.add_all([push_routine, pull_routine, leg_routine])

        squat = Exercise(name="Squats", sets=5, reps=10)
        bench_press = Exercise(name="Bench Press", sets=5, reps=5)
        deadlift = Exercise(name="Deadlift", sets=2, reps=4)
    

        push_routine.exercises.append(squat)
        push_routine.exercises.append(deadlift)

        leg_routine.exercises.append(squat) 
        leg_routine.exercises.append(deadlift) 


        db.session.add_all([push_routine, pull_routine, leg_routine, squat, bench_press, deadlift])
        db.session.commit()