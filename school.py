from student import Student
class School:
    def __init__(self,name):
        self.name = name
        self.students = []
    def add_student(self,student):
        #self.students = int(input("Enter the Student Name:\n"))
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
                print("Student deleted successfully")
                return 
        print("Student not found")
    def Topper(self):
        if not self.students:
            print("NO student found")
            return
        topper = max(self.students,key= lambda student: student.get_marks())
        print("Topper")
        topper.display()
    def save_student_data(self):
        with open ("Student_data_project","w") as f:
            for student in self.students:
                f.write(
                    f"{student.name},{student.roll_num},{student.get_marks()}\n"
                )
        print("Students saved successfully")
    def show_load(self):
        with open("Student_data_project","r")as f:
            for line in f:
                print(line.split())
        print("Successfully Showed the Students")
    def load_student(self):
        with open("Student_data_project","r") as f:
            for line in f:
                name,roll_num,marks = line.strip().split(',')
                student = Student(
                    name, int(roll_num),int(marks)
                )
                self.students.append(student)
    def rank_student(self):
        self.rank_students = sorted(
            self.students , key=lambda student: student.get_marks(),
            reverse=True
        )
        for rank, student in enumerate(self.rank_students,start=1):
            print(f"{rank}.{student.name} - {student.get_marks()}")

        
