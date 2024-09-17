from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Course,Student, Teacher
import ipdb

db_eng = create_engine('sqlite:///schools.db')
sessionObj = sessionmaker(bind=db_eng)
current_session = sessionObj()

teacher1 = Teacher(name="Peter")
teacher2 = Teacher(name = "Mercy")
teacher3 = Teacher(name="Stella")
current_session.bulk_save_objects([teacher1,teacher2,teacher3])
current_session.commit()

# tr1 = current_session.query(Teacher).first()
# tr2 = current_session.query(Teacher)[1]



ipdb.set_trace()

# create 2 courses
# create 5 students and assign them to courses

# course1 = Course(name="Software Engineering", duration="6months")
# course2 = Course(name="Data Science", duration = "5 months")


# std2 = Student(name="Student 2", age=21, fee="20000", course_id=1)
# std3 = Student(name="Student 3", age=22, fee="25000", course_id=2)
# std4 = Student(name="Student 4", age=23, fee="25000", course_id=2)
# std5 = Student(name="Student 5", age=24, fee="25000", course_id=2)
# std1 = Student(name="Student 1", age=20, fee="20000", course=course1)

# current_session.add(course1)
# current_session.add(course2)
# current_session.add(std1)
# current_session.add(std2)
# current_session.add(std3)
# current_session.add(std4)
# current_session.add(std5)

# current_session.commit()
