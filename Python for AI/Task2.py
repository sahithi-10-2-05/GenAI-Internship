def calculate_final_score(internal,external):
    total_score=internal+external

def calculate_grade(total_score):
    if(total_score>=85):
        print("A")
    elif(total_score>=70):
        print("B")
    elif(total_score>=55):
        print("C")
    elif(total_score>=40):
        print("D")
    else:
        print("fail")

class Person:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def get_role(self):
        return "Person"
    def display_details(self):
        print(self.id)
        print(self.name)

class Student(Person):
    def __init__(self,department):
        self.department=department
    def enroll_course(self,course_name):
        self.course_name=course_name
    def add_marks(self,course_name,internal,external):
        self.course_name=course_name
        self.internal=internal
        self.external=external
    def get_role():
        return "Student"
    def calculate_result(self,course_name):
        self.course_name=course_name

class Professor(Person):
    def __init__(self, department,subjects_handled):
        self.department=department
        self.subjects_handled=subjects_handled
    def assign_marks(self,course_name,internal,external):
        self.course_name=course_name
        self.internal=internal
        self.external=external
        
    def get_role():
        return "Professor"
    
class Course:
    def __init__(self,course_name,professor,students):
        self.course_name=course_name
        self.professor=professor
        self.students=students
    def add_student(Student):
        pass
    def show_course_report(add_marks):
        pass
    
P1=Professor("CS","Python")
S1=Student("CS")
S2=Student("CS")
S1.add_marks("CS",60,40)
S2.add_marks("CS",50,50)
S1.enroll_course("CS")
S2.enroll_course("CS")
P1.assign_marks("Python",50,40)

         
    

        

        