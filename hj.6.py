class Student(object):
    pass

s = Student()
s.name = 'Michael'
print(s.name)

def set_age(self, age):
    self.age = age

def set_score(self, score):
    self.score = score
Student.set_score = set_score

from types import MethodType

s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)


s.set_score(100)
print(s.score)

s2 = Student()
s2.set_score(99)
print(s2.score)