class School:
    def __init__(self,name):
        self.name = name
        self.students = []
    def add_student(self,student):
        self.students.append(student)
    def show_student(self):
        for student in self.students:
            student.display() # We are using display from the student.py file 
            print(20*"_")

        
