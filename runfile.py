from sqlalchemy import create_engine
from models import Base, Course, Teacher
from sqlalchemy.orm import sessionmaker

our_db_engine = create_engine('sqlite:///school.db')
Base.metadata.create_all(our_db_engine)
sessionObj = sessionmaker(bind=our_db_engine)
current_session = sessionObj()

# new_course = Course(name="Software Engineering",duration="6 Months")
# current_session.add(new_course)
# current_session.commit()

# get all courses 
# yoursession.query(Model).all()
# all_courses = current_session.query(Course).all()
# print(all_courses)

tr1 = Teacher(name="Mercy")
current_session.add(tr1)
current_session.commit()




def run():
    print("What do you want?")
    print("1.Add a course")
    print("2.Add a student")
    print("3.Exit")
    choice = input("Select Option:")
    if choice == "1":
        name = input("What is the name of the course?")
        duration = input("How long is the course?")
        new_course = Course(name=name, duration=duration)
        current_session.add(new_course)
        current_session.commit()
        return "New Course Added"
    else:
        print("Bye")
        return "Bye"

# run()




