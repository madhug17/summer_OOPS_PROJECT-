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
    def search(self,roll_num):
        for student in self.students:
            if student.roll_num == roll_num:
                student.display()
                return
        print("Student not found ")
    def update_student(self,roll_num,new_marks):
        for student in self.students:
            if student.roll_num == roll_num:
                student.set_marks(new_marks)
                print("Updated the marks successfully")
                return
        print("Student not found")
    def delete_student(self,roll_num):
        for student in self.students:
            if student.roll_num == roll_num:
                self.students.remove(student)
        print("Student not found")


        
