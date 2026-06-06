from student import Student
from school import School

# Create School Object
school = School("School of Gods")

# Create Student Objects
s1 = Student("Madhu", 2079, 98)
s2 = Student("Goku", 2080, 99)
s3 = Student("Vegita", 2082, 95)
s4 = Student("Gohan", 2081, 91)
s5 = Student("Trunks", 2083, 89)
while True:
    #print("real madrid") # checking git diff 
    print("\n1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Find Topper")
    print("7. Save Data")
    print("8. Load Data")
    print("9. rank_students")
    print("10. showing student from loadfile")
    print("11. sort_student_marks ")
    print("12. Sorted_name")
    print("13. Exit")

    choice = input("Enter choice: ")
    if choice =="1":
        name = input("Enter the name:\n")
        roll_num = int(input("Student Roll_num:\n"))
        marks = int(input("Enter the marks:\n"))
        if marks < 0 or marks>100:
            print("Invalid marks. Marks must be between 0 and 100.")
        else:
           student= Student(name,roll_num,marks)
           school.add_student(student)
        #if school.add_student(student):
        #    print("Student added successfully")
        #else:
        #    print("Student not added")
        print("Student added Successful")
    elif choice == "2":
        print(20*"-")
        school.show_student()
    elif choice == "3":
        roll_num = int(input("Enter the roll_num:\n"))
        school.search(roll_num)
    elif choice=="4":
        roll_num = int(input("Enter the roll_num:\n"))
        marks= int(input("Enter the marks"))
        school.update_student(roll_num,marks)
    elif choice =="5":
        roll_num = int(input("Enter the roll_num:\n"))
        school.delete_student(roll_num)
    elif choice == "6":
        school.Topper()
    elif choice == "7":
        school.save_student_data()
    elif choice == "8":
        school.load_student()
    elif choice == '9':
        school.rank_student()
    elif choice == "10":
        school.show_load()
    elif choice == "11":
        school.sort_student_marks()
    elif choice == "12":
        school.sort_student_name()
    elif choice == "13":
        print("Bye Boi!")
        break
         
print("Main Commit 1")
print("ADDED RANKING FEATURE")
## Add Students
#school.add_student(s1)
#school.add_student(s2)
#school.add_student(s3)
#school.add_student(s4)
#school.add_student(s5)
#
#print("\n--- All Students ---")
#school.show_student()
#
#print("\n--- Update Student ---")
#school.update_student(2079, 100)
#school.show_student()
#
#print("\n--- Delete Student ---")
#school.delete_student(2083)
#school.show_student()
#
#print("\n--- Search Student ---")
#school.search(2080)
#
#print("\n--- Topper ---")
#school.Topper()
#
#print("\n--- Save Data ---")
#school.save_student_data()
#
## Clear current data to test loading
#school.students.clear()
#
#print("\n--- Load Data ---")
#school.load_student()
#
#print("\n--- Students After Loading ---")
#school.show_student()