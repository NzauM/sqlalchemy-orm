from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from uuid import uuid4
from sqlalchemy.ext.associationproxy import association_proxy

Base = declarative_base()

class Course(Base):
    # A course has many students

    __tablename__ = 'courses'

    id = Column(Integer(), primary_key = True)
    name = Column(String())
    duration = Column(String())

    # teachers
    # teacher_id = list

    students = relationship('Student',  backref="course")
    lectures = relationship('Lecture', back_populates="course")
    teachers = association_proxy('lectures','teacher',creator=lambda tr: Lecture(teacher=tr))

    # relationship = association_proxy('jointablerelationship','secondclass', creator=Lecture(teacher = ))


    def __repr__(self):
        return f"Course {self.id}: {self.name} duration {self.duration}"
    pass

class Student(Base):
    # A student has one course

    __tablename__ = "students"

    id = Column(Integer(),primary_key = True)
    name = Column(String())
    age = Column(Integer())
    fee = Column(String())
    course_id = Column(Integer(), ForeignKey('courses.id'))


class Teacher(Base):
    __tablename__ = "teachers"
    
    id = Column(String(), primary_key=True, default=lambda: str(uuid4()))
    name = Column(String())

    lectures = relationship('Lecture', back_populates='teacher')
    courses = association_proxy('lectures','course', creator=lambda course: Lecture(course = course))

    # courses
    # course_id = list

# employee created with name and id_no
class Employee(Base):

    __tablename__ = 'employees'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    id_no = Column(Integer())
    bank = Column(String())
    department = Column(String())


class Lecture(Base):
    # an association object between teachers and courses
    __tablename__ = 'lectures'

    id = Column(Integer(), primary_key=True)
    teacher_id = Column(Integer(), ForeignKey('teachers.id'))
    course_id = Column(Integer(), ForeignKey('courses.id'))
    topic = Column(String())
    hours = Column(Integer())
    salary = Column(Integer())

    teacher = relationship('Teacher',back_populates='lectures')
    course = relationship('Course', back_populates='lectures')

    # Lecture to Teacher => One to Many
    # Lecture to Course => One to Many
    # Teacher to Course => Many to Many








    


# Coffee => name  
# Customer => name
# Order => cofee 
# Order => customer, price





