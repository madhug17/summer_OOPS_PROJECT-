from student import Student


class School:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        for s in self.students:
            if s.roll_num == student.roll_num:
                print("Roll number already exists")
                return

        self.students.append(student)
        print("Student added successfully")

    def show_student(self):
        for student in self.students:
            student.display()
            print("_" * 20)

    def search(self, roll_num):
        for student in self.students:
            if student.roll_num == roll_num:
                student.display()
                return

        print("Student not found")

    def update_student(self, roll_num, new_marks):
        for student in self.students:
            if student.roll_num == roll_num:
                student.set_marks(new_marks)
                print("Updated marks successfully")
                return

        print("Student not found")

    def delete_student(self, roll_num):
        for student in self.students:
            if student.roll_num == roll_num:
                self.students.remove(student)
                print("Student deleted successfully")
                return

        print("Student not found")

    def Topper(self):
        if not self.students:
            print("No students found")
            return

        topper = max(
            self.students,
            key=lambda student: student.get_marks()
        )

        print("Topper:")
        topper.display()

    def rank_student(self):
        ranked_students = sorted(
            self.students,
            key=lambda student: student.get_marks(),
            reverse=True
        )

        for rank, student in enumerate(ranked_students, start=1):
            print(f"{rank}. {student.name} - {student.get_marks()}")

    def sort_student_marks(self):
        if not self.students:
            print("No students to sort")
            return

        sorted_marks = sorted(
            self.students,
            key=lambda student: student.get_marks(),
            reverse=True
        )

        print("Students sorted by marks:")

        for student in sorted_marks:
            student.display()

    def save_student_data(self):
        with open("Student_data_project", "w") as f:
            for student in self.students:
                f.write(
                    f"{student.name},{student.roll_num},{student.get_marks()}\n"
                )

        print("Students saved successfully")

    def load_student(self):
        with open("Student_data_project", "r") as f:
            for line in f:
                name, roll_num, marks = line.strip().split(",")

                student = Student(
                    name,
                    int(roll_num),
                    int(marks)
                )

                self.students.append(student)

        print("Students loaded successfully")

    def show_load(self):
        with open("Student_data_project", "r") as f:
            for line in f:
                print(line.strip())
    def sort_student_name(self):
        sort_name = sorted(self.students,key=lambda student:student.name.lower())
        for student in sort_name:
            student.display()