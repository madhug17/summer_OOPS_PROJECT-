from student import Student  # the student is file name and Student is Class name That is the format man 
from school import School

School = School("School of Gods")
s1 = Student ("Madhu",2079,98)
s2 = Student ("Goku",2080,99)
s3 = Student ("Vegita",2082,95)
s4 = Student ("Gohan",2081,91)
s5 = Student ("Trunks",2083,89)

School.add_student(s1)
#School.add_student(s2)
#School.add_student(s3)
#School.add_student(s4)
#School.add_student(s5)
School.show_student()
School.update_student("2079",99)
School.show_student()