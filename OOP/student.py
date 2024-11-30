class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def get_grade(self):
        return self.grade
        
class Course:
    def __init__(self, name,max_students):
        self.name = name
        self.max_students = max_students
        self.students=[]
        
    def add_students(self, Student):
        if len(self.students)<self.max_students:
            self.students.append(Student)
            return True
        print(self.students)
        return False
    
    def get_average(self):
        value=0
        for student in self.students:
            value+=student.get_grade()
        print(abs(value/len(self.students)))
s1=Student("Shyaam",12,3)
s2=Student("Hari",12,7)
s3=Student("Komi",13,5)
course=Course("Science",2)
course.add_students(s1)
course.add_students(s2)
course.add_students(s3)
course.get_average()