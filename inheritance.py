# Parent class
class Parent:
    def __init__(self, father_name, mother_name):
        self.father_name = father_name
        self.mother_name = mother_name

    def display_parent_details(self):
        print("Father Name:", self.father_name)
        print("Mother Name:", self.mother_name)


# Child class inheriting Parent class
class Student(Parent):
    def __init__(self, student_name, roll_no, father_name, mother_name):
        super().__init__(father_name, mother_name)  # Inherit parent details
        self.student_name = student_name
        self.roll_no = roll_no

    def display_student_details(self):
        print("Student Name:", self.student_name)
        print("Roll Number:", self.roll_no)
        self.display_parent_details()


# Creating object of Student class
s1 = Student("prashamsha", 10, "Narayan ", "Laxmi")

# Display details
s1.display_student_details()