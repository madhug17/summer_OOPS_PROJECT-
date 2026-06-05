class Student:
    def __init__(self,name, roll_num,marks):
        self.name = name
        self.roll_num= roll_num
        self.__mark = marks
    def get_marks(self):
        return self.__mark
    def set_marks(self,marks):
        if 0 <= marks <= 100:
            self.__mark = marks
    def display(self):
        print(f"Name of the student:",self.name)
        print(f"Roll_nums of Student:",self.roll_num)
        print(f"Marks:",self.__mark)
