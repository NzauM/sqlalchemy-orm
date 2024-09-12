from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from uuid import uuid4

Base = declarative_base()

class Course(Base):

    __tablename__ = 'courses'

    id = Column(Integer(), primary_key = True)
    name = Column(String())
    duration = Column(String())

    def __repr__(self):
        return f"Course {self.id}: {self.name} duration {self.duration}"




    pass

class Student(Base):

    __tablename__ = "students"

    id = Column(Integer(),primary_key = True)
    name = Column(String())
    age = Column(Integer())

class Teacher(Base):
    __tablename__ = "teachers"
    
    id = Column(Integer(), primary_key=True, default=uuid4)
    name = Column(String())
    


