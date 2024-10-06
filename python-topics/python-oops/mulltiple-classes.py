class Student:

    def __init__(self,name,grade,age):
        self.name = name 
        self.grade = grade
        self.age = age
    
    def get_grade(self):
        return self.grade 
    
class Course:

    def __init__(self,name,max_students):
        self.name = name
        self.max_student = max_students
        self.students = []

    def add_student(self,student):
        if len(self.students) < self.max_student:
           self.students.append(student)
           print(self.students) 
           return True
        return False

    def average_grade(self):
        value = 0
        for student in self.students:
             value += student.get_grade()
        return value / len(self.students)
    
s1 = Student("tim",95,16) 
s2 = Student("sam",85,16)
s3 = Student("kim",65,16)

course = Course("science",2)
course.add_student(s1)
course.add_student(s2)
print(course.average_grade()) 

